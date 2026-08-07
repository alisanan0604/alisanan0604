import React from 'react'

const GREEN = '#3ddc84'
const TEAL = '#00e5c0'
const BG = '#0c1014'
const CARD_BG = '#131a1f'
const TERMINAL_BG = '#0a0d11'
const TEXT = '#c9d1d9'
const MUTED = '#6e7681'
const SECTION_BORDER = '#1a3d2b'

function TerminalWindow({ title, children }: { title: string; children: React.ReactNode }) {
return (
<div style={{
      background: TERMINAL_BG,
      border: '1px solid #1e262e',
      borderRadius: 8,
      overflow: 'hidden',
      fontFamily: "'JetBrains Mono', 'Courier New', monospace",
      fontSize: 13,
    }}>
<div style={{
        background: '#111820',
        borderBottom: '1px solid #1e262e',
        padding: '8px 12px',
        display: 'flex',
        alignItems: 'center',
        gap: 8,
      }}>
<span style={{ width: 12, height: 12, borderRadius: '50%', background: '#ff5f57', display: 'inline-block' }} />
<span style={{ width: 12, height: 12, borderRadius: '50%', background: '#febc2e', display: 'inline-block' }} />
<span style={{ width: 12, height: 12, borderRadius: '50%', background: '#28c840', display: 'inline-block' }} />
<span style={{ flex: 1, textAlign: 'center', color: MUTED, fontSize: 12 }}>{title}</span>
</div>
<div style={{ padding: '16px 20px', color: TEXT, lineHeight: 1.7 }}>
{children}
</div>
</div>
)
}

function Prompt({ cmd }: { cmd: string }) {
return (
<div style={{ marginBottom: 4 }}>
<span style={{ color: GREEN, fontWeight: 600 }}>alisanan0604@github</span>
<span style={{ color: TEXT }}> :~$ </span>
<span style={{ color: TEXT }}>{cmd}</span>
</div>
)
}

function SectionHeader({ label }: { label: string }) {
return (
<div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 16 }}>
<span style={{ color: MUTED, fontSize: 16 }}>⠿</span>
<span style={{ color: GREEN, fontWeight: 700, fontSize: 12, letterSpacing: '0.1em' }}>{label}</span>
</div>
)
}

function Section({ label, children }: { label: string; children: React.ReactNode }) {
return (
<div style={{
      border: `1px solid ${SECTION_BORDER}`,
      borderRadius: 10,
      padding: '20px 24px',
      marginBottom: 24,
      background: CARD_BG,
    }}>
<SectionHeader label={label} />
{children}
</div>
)
}

function Pill({ label }: { label: string }) {
return (
<span style={{
      border: `1px solid ${GREEN}`,
      borderRadius: 20,
      padding: '4px 14px',
      color: GREEN,
      fontSize: 13,
      fontWeight: 600,
      fontFamily: "'Inter', sans-serif",
    }}>{label}</span>
)
}

function Tag({ label }: { label: string }) {
return (
<span style={{
      border: '1px solid #2a3a45',
      borderRadius: 20,
      padding: '3px 12px',
      color: TEXT,
      fontSize: 12,
      background: '#141c24',
    }}>{label}</span>
)
}

function ContributionGrid() {
const weeks = 52
const days = 7
const cells = []
const activeDays: Record<string, string> = {
'49-0': TEAL,
'50-2': '#5bc4a8',
'50-4': TEAL,
'50-5': GREEN,
}
for (let w = 0; w < weeks; w++) {
for (let d = 0; d < days; d++) {
const key = `${w}-${d}`
cells.push(
<div key={key} style={{
          width: 11,
          height: 11,
          borderRadius: 2,
          background: activeDays[key] || '#1a2530',
        }} />
)
}
}
return (
<div>
<div style={{
        display: 'grid',
        gridTemplateColumns: `repeat(${weeks}, 11px)`,
        gridTemplateRows: `repeat(${days}, 11px)`,
        gap: 3,
        marginBottom: 10,
        overflowX: 'auto',
      }}>
{cells}
</div>
<div style={{ color: MUTED, fontSize: 12, fontFamily: "'JetBrains Mono', monospace" }}>32 contributions in the last year</div>
</div>
)
}

function StatTile({ value, label }: { value: string; label: string }) {
return (
<div style={{
      background: '#111820',
      border: '1px solid #1e262e',
      borderRadius: 8,
      padding: '20px 24px',
      flex: 1,
      textAlign: 'center',
    }}>
<div style={{ fontWeight: 700, fontSize: 22, color: TEXT, marginBottom: 4 }}>{value}</div>
<div style={{ color: MUTED, fontSize: 12, letterSpacing: '0.08em' }}>{label}</div>
</div>
)
}

function ProjectCard({ name, desc, tags }: { name: string; desc: string; tags: string[] }) {
return (
<div style={{
      background: '#111820',
      border: '1px solid #1e262e',
      borderRadius: 8,
      padding: '20px 22px',
      flex: 1,
    }}>
<div style={{ fontWeight: 700, fontSize: 15, color: TEXT, marginBottom: 8 }}>{name}</div>
<div style={{ color: MUTED, fontSize: 13, marginBottom: 14, lineHeight: 1.6 }}>{desc}</div>
<div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
{tags.map(t => <Tag key={t} label={t} />)}
</div>
</div>
)
}

const SANAN_ALI_ASCII = `
 SSSSSSSSS  SSSSSS   SSSS  SS  SSSSS   SSSS        SSSSSSS   LL      IIIIIII
SS+++++++S  S+++SS  SS++SS SS  S+++SS  SS+SS       SS   SS   LL        III
SS          SS   SS  SSSSS  SS  SS   SS SS SS      SS   SS   LL        III
SSSSSSSSSS  SSSSSS   SSSS   SS  SSSSSS  SS SS      SSSSSSS   LL        III
       +SS SS   SS  SS SS  SS  SS   SS SS SS       SS   SS   LL        III
SS+++++++S SS    SS SS  SS SS  SS    SS SS++SS     SS   +S   LL        III
SSSSSSSSS  SS    SS SS  SSSS  SS    SS SSSSSS      SS   SS   LLLLLLL IIIIIII`.trim()

const PORTRAIT_ASCII = `
```text
@@@@@@@@@@@%%@%%@@@@%%%%%%%%%%%%%%%####%##*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%%%%%@@@@@@@@@@@@@@@@@@@@%%%%%%%
@@@@@@@@@@@@%%%@@%@@%%%%%%%%%%%%%%#########%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##%%%%%@%%%%%@@@@@@@@@@@@@@@@@@@%%%%%%%%
@@@@@@@@@@%%%%%@%@%%%%%%%%%%%%%%%###*%%%##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@%%%%%%%%
...
````.trim()

export default function App() {
return (
<div style={{ background: BG, minHeight: '100vh', color: TEXT, fontFamily: "'Inter', sans-serif" }}>
<div style={{ maxWidth: 900, margin: '0 auto', padding: '32px 24px 0' }}>

        {/* Profile header */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 24, marginBottom: 32, paddingBottom: 32, borderBottom: '1px solid #1e2a35' }}>
          <div style={{
            width: 80, height: 80, borderRadius: '50%',
            background: 'linear-gradient(135deg, #1a2030 0%, #2a1520 100%)',
            border: '2px solid #2a3a45',
            overflow: 'hidden',
            flexShrink: 0,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontSize: 32,
          }}>👤</div>
          <div>
            <div style={{ fontSize: 36, fontWeight: 700, color: TEXT, lineHeight: 1.1, marginBottom: 8 }}>alisanan0604</div>
            <div style={{ color: MUTED, fontSize: 14 }}>Memorable developer positioning. Built with the Aurora GitSkins visual system.</div>
          </div>
        </div>

        {/* HEADER section */}
        <Section label="HEADER">
          <TerminalWindow title="alisanan0604@github: ~ — -zsh">
            <Prompt cmd="whoami" />
            <div style={{ marginBottom: 12 }}>
              <div style={{ fontWeight: 700, fontSize: 16, color: TEXT }}>Sanan Ali</div>
              <div style={{ color: GREEN, fontSize: 13 }}>Developer</div>
            </div>
            <Prompt cmd="cat bio.txt" />
            <div style={{ marginBottom: 12, color: TEXT, fontFamily: "'JetBrains Mono', monospace", fontSize: 13 }}>
              Building with code on GitHub.
            </div>
            <Prompt cmd="" />
          </TerminalWindow>
        </Section>

        {/* ASCII art panels */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16, marginBottom: 24 }}>
          {/* SANAN ALI wordmark */}
          <TerminalWindow title="alisanan0604@github: ~$ ./wordmark.sh --name">
            <pre style={{
              fontSize: 9,
              lineHeight: 1.35,
              color: GREEN,
              overflowX: 'auto',
              margin: 0,
              fontFamily: "'JetBrains Mono', monospace",
            }}>{SANAN_ALI_ASCII}</pre>
          </TerminalWindow>

          {/* Portrait */}
          <TerminalWindow title="alisanan0604@github: ~$ ./portrait.sh">
            <pre style={{
              fontSize: 9,
              lineHeight: 1.3,
              color: GREEN,
              margin: 0,
              textAlign: 'center',
              fontFamily: "'JetBrains Mono', monospace",
            }}>{PORTRAIT_ASCII}</pre>
          </TerminalWindow>
        </div>

        {/* Intro text */}
        <p style={{ color: TEXT, fontSize: 14, marginBottom: 24, lineHeight: 1.7 }}>
          Hi, I&apos;m <strong>alisanan0604</strong>, a full-stack engineer focused on memorable developer positioning.
        </p>

        {/* ABOUT ME */}
        <Section label="ABOUT ME">
          <TerminalWindow title="alisanan0604@github: ~$ cat about.md">
            <Prompt cmd="cat about.md" />
            <div style={{ marginBottom: 16, fontFamily: "'JetBrains Mono', monospace", fontSize: 13 }}>Engineer building with code.</div>
            <div style={{ color: MUTED, fontFamily: "'JetBrains Mono', monospace", fontSize: 13 }}>&gt; open to collaboration</div>
          </TerminalWindow>
          <div style={{
            background: '#111820',
            border: '1px solid #1e262e',
            borderRadius: 8,
            padding: '18px 20px',
            marginTop: 16,
          }}>
            <div style={{ fontWeight: 700, fontSize: 15, color: TEXT, marginBottom: 6 }}>Full-Stack Engineer</div>
            <div style={{ color: MUTED, fontSize: 13, lineHeight: 1.6 }}>
              Shapes the short profile story and positioning. The copy is tuned for a confident tone and a creative README.
            </div>
          </div>
        </Section>

        {/* SKILLS */}
        <Section label="SKILLS">
          <TerminalWindow title="alisanan0604@github: ~$ ls skills/">
            <Prompt cmd="ls skills/" />
            <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap', marginTop: 4 }}>
              {['TypeScript', 'React', 'Go', 'Rust'].map(s => (
                <span key={s} style={{
                  border: '1px solid #2a3a45',
                  borderRadius: 4,
                  padding: '2px 12px',
                  color: TEXT,
                  fontSize: 13,
                  fontFamily: "'JetBrains Mono', monospace",
                }}>{s}</span>
              ))}
            </div>
          </TerminalWindow>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10, marginTop: 16 }}>
            {['TypeScript', 'Next.js', 'React', 'Node.js', 'Product Engineering'].map(s => (
              <Pill key={s} label={s} />
            ))}
          </div>
        </Section>

        {/* GITHUB STATS */}
        <Section label="GITHUB STATS">
          <TerminalWindow title="alisanan0604@github: ~$ neofetch">
            <div style={{ display: 'flex', gap: 32 }}>
              <div style={{ fontFamily: "'JetBrains Mono', monospace", color: TEAL, fontSize: 12, lineHeight: 1.8, whiteSpace: 'pre', flexShrink: 0 }}>

{` ___________
| -- -- |
| · github|
| > _  |
|___________|`}
</div>
<div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 13 }}>
<div style={{ marginBottom: 8 }}>
<span style={{ color: TEAL, fontWeight: 700 }}>alisanan0604</span>
<span style={{ color: MUTED }}> @github</span>
</div>
<div style={{ borderBottom: '1px solid #2a3a45', marginBottom: 8 }} />
{[
['Name', 'Sanan Ali'],
['Role', 'Developer'],
['Stars', '0'],
['Repos', '2'],
['Followers', '0'],
['Top Lang', '—'],
['Activity', '32 contributions'],
].map(([k, v]) => (
<div key={k} style={{ display: 'flex', gap: 16, marginBottom: 4 }}>
<span style={{ color: TEAL, minWidth: 90 }}>{k}</span>
<span style={{ color: TEXT }}>{v}</span>
</div>
))}
<div style={{ display: 'flex', gap: 6, marginTop: 12 }}>
{['#3ddc84', '#00bcd4', '#5c6bc0', '#ab47bc', '#ec407a', '#3ddc84'].map((c, i) => (
<div key={i} style={{ width: 22, height: 22, background: c, borderRadius: 3 }} />
))}
</div>
</div>
</div>
</TerminalWindow>
<div style={{ display: 'flex', gap: 16, marginTop: 16 }}>
<StatTile value="Aurora" label="THEME" />
<StatTile value="playful" label="MOTION" />
<StatTile value="8" label="SECTIONS" />
</div>
</Section>

        {/* PROJECTS */}
        <Section label="PROJECTS">
          <TerminalWindow title="alisanan0604@github: ~$ ls -la repos/">
            <Prompt cmd="ls -la repos/" />
            <div style={{ color: TEXT, fontFamily: "'JetBrains Mono', monospace", fontSize: 13 }}>awesome-project</div>
          </TerminalWindow>
          <div style={{ display: 'flex', gap: 16, marginTop: 16, flexWrap: 'wrap' }}>
            <ProjectCard
              name="alisanan0604-studio"
              desc="A personal brand project with clear outcomes and a polished product surface."
              tags={['TypeScript', 'Next.js', 'React']}
            />
            <ProjectCard
              name="developer-tools"
              desc="Reusable systems, automation, and GitHub-native workflow improvements."
              tags={['React', 'Node.js', 'Product Engineering']}
            />
          </div>
        </Section>

        {/* HIGHLIGHTS */}
        <Section label="HIGHLIGHTS">
          <TerminalWindow title="alisanan0604@github: ~$ cat highlights.txt">
            <Prompt cmd="cat highlights.txt" />
            <div style={{ color: TEXT, fontFamily: "'JetBrains Mono', monospace", fontSize: 13, lineHeight: 1.8 }}>
              <div>→ Built and shipped full-stack products end-to-end</div>
              <div>→ Open source contributor across React + TypeScript ecosystem</div>
              <div>→ Focused on clean architecture and developer experience</div>
            </div>
          </TerminalWindow>
        </Section>

        {/* HEATMAP */}
        <Section label="HEATMAP">
          <TerminalWindow title="alisanan0604@github: ~$ ./contributions.sh">
            <Prompt cmd="./contributions.sh" />
            <ContributionGrid />
          </TerminalWindow>
        </Section>

        {/* CONNECT */}
        <Section label="CONNECT">
          <TerminalWindow title="alisanan0604@github: ~$ ./links.sh">
            <Prompt cmd="./links.sh" />
            <div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 13, color: TEXT }}>
              GitHub &nbsp; github.com/alisanan0604
            </div>
          </TerminalWindow>
        </Section>

        {/* Footer */}
        <p style={{ color: MUTED, fontSize: 14, paddingBottom: 48 }}>
          Let&apos;s build something useful together.
        </p>
      </div>
    </div>

)
}
