#!/usr/bin/env python3
"""
parse_library.py
Converts a Rekordbox XML export into library.json for the set planner.

Usage:
    python3 parse_library.py RKlibrary.xml
"""

import xml.etree.ElementTree as ET
import json
import sys
import os

def parse(xml_path):
    print(f"Parsing {xml_path}...")
    tree = ET.parse(xml_path)
    root = tree.getroot()
    collection = root.find('COLLECTION')

    tracks = []
    skipped = 0

    for track in collection:
        name = track.get('Name', '').strip()
        key  = track.get('Tonality', '').strip()
        bpm_str = track.get('AverageBpm', '0')

        if not name or not key:
            skipped += 1
            continue

        try:
            bpm = round(float(bpm_str), 1)
        except ValueError:
            bpm = 0.0

        tracks.append({
            'id':         track.get('TrackID', ''),
            'name':       name,
            'artist':     track.get('Artist', '').strip(),
            'bpm':        bpm,
            'key':        key,
            'genre':      track.get('Genre', '').strip(),
            'duration':   int(track.get('TotalTime', 0)),
            'play_count': int(track.get('PlayCount', 0)),
            'date_added': track.get('DateAdded', ''),
        })

    out = {
        'tracks': tracks,
        'total':  len(tracks),
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'library.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False)

    print(f"Done. {len(tracks)} tracks saved to {out_path}")
    if skipped:
        print(f"  ({skipped} tracks skipped — missing name or key)")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 parse_library.py <path_to_RKlibrary.xml>")
        sys.exit(1)
    parse(sys.argv[1])
