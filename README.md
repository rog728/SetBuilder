# TrackSuggester

A web-based DJ set planner that helps you build musical sets with harmonic mixing guidance.

## Features

- **Harmonic Mixing**: Visual indicators for key compatibility between tracks
- **Rainbow Key Colors**: Each Camelot key is displayed in its corresponding rainbow color
- **BPM Filtering**: Filter tracks by BPM range
- **Set Planning**: Build and manage your set with transition indicators
- **Search & Sort**: Find tracks by name/artist, sort by various criteria

## Setup

1. **Parse your Rekordbox library** (optional - see demo below):
   ```bash
   python3 parse_library.py RKlibrary.xml
   ```

2. **Start the web server**:
   ```bash
   python3 -m http.server 8000
   ```

3. **Open in browser**:
   Visit `http://localhost:8000/index.html`

## Demo

For demonstration purposes, a sample library is included:

```bash
python3 parse_library.py sample_library.xml
```

This creates `library.json` with 8 sample tracks spanning keys 1A through 8A, perfect for showcasing the rainbow color feature.

## File Structure

- `parse_library.py` - Converts Rekordbox XML to JSON
- `index.html` - Main web interface
- `sample_library.xml` - Demo data (safe to commit)
- `RKlibrary.xml` - Your personal library (ignored by git)
- `library.json` - Processed track data (ignored by git)

## Privacy

Your personal music library data (`RKlibrary.xml` and `library.json`) are ignored by git and never committed. Only the demo sample is included in the repository.