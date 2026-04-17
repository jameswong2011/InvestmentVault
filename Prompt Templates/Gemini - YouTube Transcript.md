# Gemini — YouTube Transcript Prompt

## Usage

1. Open Gemini and paste the YouTube URL
2. Copy the prompt below and paste it after the URL
3. Save Gemini's output as `YYYY-MM-DD - [Topic] - video-transcript.md` in `_Inbox/`
4. Run `/ingest` to process into a Research note

---

## Prompt

```
Transcribe this YouTube video (https://www.youtube.com/watch?v=Hrbq66XqtCo) in full. Output in the exact format below — no deviations, no additions. Save your output as a .md file (in this format: `[Video Upload Date in `YYYY-MM-DD format] - [Channel Name | Video Title] - video-transcript.md`) that can be downloaded.

  

Start with this YAML frontmatter block (fill in every field):

  

date: [YYYY-MM-DD]

source: [the YouTube URL]

source_type: video-transcript

channel: [YouTube channel name]

video title: [Video title]

speakers: [comma-separated list of speakers identified in the video]

topics: [3-5 keyword tags describing the core subjects covered]

duration: [video length in MM:SS or HH:MM:SS]

  

Then two sections:

  

Summary

3-5 sentences describing what the video covers. No analysis or opinion — just scope and subject matter. Include who is speaking and in what context (interview, presentation, panel, podcast, etc.).

  

Transcript

The full transcript of the video. Follow these rules exactly:

  

Label speakers in bold where identifiable (e.g., Host:, Jensen Huang:). If a speaker's name is unknown, use a consistent label (e.g., Interviewer:, Guest:).

Insert paragraph breaks at natural topic shifts — do not output a wall of text.

Preserve exact phrasing, numbers, company names, ticker symbols, and financial terminology. Do not paraphrase or clean up spoken language beyond basic readability.

Do not add timestamps.

Do not add section headers within the transcript.

Do not add commentary, annotations, or analysis.

If a word or phrase is unclear in the audio, write [inaudible] rather than guessing.
```
