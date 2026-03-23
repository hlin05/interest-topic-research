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

## Adding a Topic

```bash
./add-topic.sh "Your Topic Name"
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
