-- ============================================================
-- 🥋 11 — DOJO V2 MIGRATION (Safe Additive — Production)
-- ============================================================
-- SAFE TO RUN: All operations are additive (ADD COLUMN IF NOT EXISTS,
-- CREATE OR REPLACE). No data is deleted or modified.
-- Run this in the Supabase SQL Editor.
-- ============================================================

-- ── 1. Store code content as text alongside the file ──
-- This avoids repeated Storage downloads for code preview.
-- Existing rows will have NULL (handled gracefully by the frontend).
ALTER TABLE public.competition_submissions
ADD COLUMN IF NOT EXISTS code_content TEXT;

COMMENT ON COLUMN public.competition_submissions.code_content IS
  'Plain text content of the .py file, stored at upload time for fast preview. '
  'The original file remains in Storage for download.';

-- ── 2. Activate real dojo_xp triggers ──
-- The column dojo_xp already exists in competition_participants.
-- We create triggers to increment it automatically.

-- 2a. Award dojo_xp when a user submits a solution (+50 dojo XP)
CREATE OR REPLACE FUNCTION public.trigger_dojo_submission_xp()
RETURNS TRIGGER AS $$
BEGIN
  -- Award 50 dojo XP for submitting a solution
  UPDATE public.competition_participants
  SET dojo_xp = COALESCE(dojo_xp, 0) + 50
  WHERE competition_id = NEW.competition_id
    AND user_id = NEW.user_id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_submission_dojo_xp ON public.competition_submissions;
CREATE TRIGGER on_submission_dojo_xp
  AFTER INSERT ON public.competition_submissions
  FOR EACH ROW EXECUTE FUNCTION public.trigger_dojo_submission_xp();

-- 2b. Award dojo_xp when a user's solution receives a like (+10 dojo XP to author)
CREATE OR REPLACE FUNCTION public.trigger_dojo_vote_xp()
RETURNS TRIGGER AS $$
DECLARE
  v_author_id UUID;
  v_comp_id UUID;
BEGIN
  IF NEW.vote = 1 THEN
    -- Find the author and competition of this submission
    SELECT user_id, competition_id INTO v_author_id, v_comp_id
    FROM public.competition_submissions
    WHERE id = NEW.submission_id;

    IF v_author_id IS NOT NULL AND v_author_id != NEW.user_id THEN
      UPDATE public.competition_participants
      SET dojo_xp = COALESCE(dojo_xp, 0) + 10
      WHERE competition_id = v_comp_id
        AND user_id = v_author_id;
    END IF;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_vote_dojo_xp ON public.competition_votes;
CREATE TRIGGER on_vote_dojo_xp
  AFTER INSERT ON public.competition_votes
  FOR EACH ROW EXECUTE FUNCTION public.trigger_dojo_vote_xp();

-- 2c. Award dojo_xp when a user posts on the wall (+5 dojo XP)
CREATE OR REPLACE FUNCTION public.trigger_dojo_wall_xp()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE public.competition_participants
  SET dojo_xp = COALESCE(dojo_xp, 0) + 5
  WHERE competition_id = NEW.competition_id
    AND user_id = NEW.user_id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_wall_post_dojo_xp ON public.competition_wall_posts;
CREATE TRIGGER on_wall_post_dojo_xp
  AFTER INSERT ON public.competition_wall_posts
  FOR EACH ROW EXECUTE FUNCTION public.trigger_dojo_wall_xp();

-- 2d. Award dojo_xp when a user comments on a solution (+5 dojo XP)
CREATE OR REPLACE FUNCTION public.trigger_dojo_comment_xp()
RETURNS TRIGGER AS $$
DECLARE
  v_comp_id UUID;
BEGIN
  -- Find the competition via submission → competition_id
  SELECT competition_id INTO v_comp_id
  FROM public.competition_submissions
  WHERE id = NEW.submission_id;

  IF v_comp_id IS NOT NULL THEN
    UPDATE public.competition_participants
    SET dojo_xp = COALESCE(dojo_xp, 0) + 5
    WHERE competition_id = v_comp_id
      AND user_id = NEW.user_id;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_comment_dojo_xp ON public.submission_comments;
CREATE TRIGGER on_comment_dojo_xp
  AFTER INSERT ON public.submission_comments
  FOR EACH ROW EXECUTE FUNCTION public.trigger_dojo_comment_xp();

-- ============================================================
-- ✅ MIGRATION COMPLETE — No existing data was modified.
-- New triggers will fire on future inserts only.
-- ============================================================
