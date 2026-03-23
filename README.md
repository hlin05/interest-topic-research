# Research Topics

Automated research agent system that scouts, curates, and maintains awesome lists across multiple topics using AI-powered signal collection and curation.

## How It Works

Each topic has its own curated awesome list maintained by a weekly Research Assistant Agent:

1. **Grok Scout** — collects recent social signals via xAI API
2. **arXiv Scout** — pulls recent papers from topic-specific RSS feeds
3. **Claude Curation** — evaluates candidates against topic-specific criteria using Anthropic Claude

## Topics

| Topic | Description |
|-------|-------------|
| [Agentic ML](topics/agentic-ml/) | Autonomous AI systems for ML workflows |
| [Agentic Workflow Design](topics/agentic-workflow-design/) | Patterns, principles, and practices for production-grade agentic systems |

## Prerequisites

| Requirement | Used by | Notes |
|-------------|---------|-------|
| `ANTHROPIC_API_KEY` | `add-topic.sh`, weekly curation | Claude deduplication and curation |
| `XAI_API_KEY` | Weekly workflow (Grok Scout) | GitHub repository secret |
| `XAI_BASE_URL` | Weekly workflow | Repository variable, default: `https://api.x.ai` |
| `GROK_MODEL` | Weekly workflow | Repository variable, default: `grok-4-1-fast-reasoning` |
| [`gh` CLI](https://cli.github.com/) | `add-topic.sh` | For GitHub Project board creation |

For local use, set `ANTHROPIC_API_KEY` in your environment before running `add-topic.sh`.

## Adding a Topic

```bash
./add-topic.sh "Your Topic Name"
./add-topic.sh "Your Topic Name" --max-entries 3   # limit weekly additions (default: 5)
```

The CLI will:
- Check for overlap with existing topics
- Generate topic-specific search keywords, RSS feeds, and inclusion criteria
- Create a GitHub Project board for tracking
- Scaffold the topic folder with a starter README

## Configuration

Topics are configured in [`topics.yml`](topics.yml). Each topic defines:
- Search keywords for social signal scouting
- arXiv RSS feed categories
- Inclusion/exclusion criteria for curation

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
