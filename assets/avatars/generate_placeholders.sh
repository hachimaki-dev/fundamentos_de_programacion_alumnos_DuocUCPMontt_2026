#!/bin/bash
# Generate SVG placeholder avatars for missing ones
declare -A AVATARS=(
  ["dev-02"]="💻|#1a1a2e|#00f5d4|Hacker"
  ["dev-04"]="⚡|#2d1b69|#ff6b9d|Full Stack"
  ["gaming-01"]="🎮|#1b2838|#66c0f4|Gamer"
  ["gaming-02"]="👾|#2a0845|#ff6b9d|Pixel Hero"
  ["gaming-03"]="🕹️|#0d1b2a|#e0e1dd|Controller"
  ["gaming-04"]="🏆|#1a1a2e|#ffd60a|Arcade"
  ["kawaii-01"]="🐱|#fce4ec|#ad1457|Kawaii Cat"
  ["kawaii-02"]="🤖|#e1bee7|#7b1fa2|Kawaii Bot"
  ["kawaii-03"]="⭐|#fff9c4|#f57f17|Kawaii Star"
  ["kawaii-04"]="☁️|#b3e5fc|#0277bd|Kawaii Cloud"
  ["robot-01"]="🤖|#0a0a0a|#00f5d4|Robot Coder"
  ["robot-02"]="🧠|#1a0a3e|#a764ff|AI Bot"
  ["robot-03"]="⚙️|#263238|#80cbc4|Mech Dev"
  ["robot-04"]="🔌|#0d0221|#ff6b9d|Cyber Bot"
  ["space-01"]="🧑‍🚀|#0d0221|#00f5d4|Astronaut"
  ["space-02"]="🚀|#1a0a3e|#ff6b9d|Rocket"
  ["space-03"]="🪐|#0f2027|#ffd60a|Planet"
  ["space-04"]="🌌|#0d0221|#a764ff|Galaxy"
)

for name in "${!AVATARS[@]}"; do
  IFS='|' read -r emoji bg accent label <<< "${AVATARS[$name]}"
  if [ ! -f "${name}.webp" ]; then
    cat > "${name}.svg" << EOF
<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
  <defs>
    <radialGradient id="g" cx="50%" cy="40%">
      <stop offset="0%" stop-color="${accent}" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="${bg}"/>
    </radialGradient>
  </defs>
  <rect width="256" height="256" rx="48" fill="${bg}"/>
  <rect width="256" height="256" rx="48" fill="url(#g)"/>
  <text x="128" y="125" text-anchor="middle" dominant-baseline="central" font-size="80">${emoji}</text>
  <text x="128" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="16" font-weight="bold" fill="${accent}" opacity="0.8">${label}</text>
</svg>
EOF
    # Copy SVG as the webp placeholder
    cp "${name}.svg" "${name}.webp"
    echo "Created ${name}"
  fi
done
echo "Done!"
