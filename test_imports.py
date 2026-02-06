#!/usr/bin/env python3
"""Test all imports in the project."""

def test_imports():
    errors = []
    
    tests = [
        ("handlers.speaker_handlers", "router"),
        ("handlers.speakers_brief", "router"),
        ("parsers.vk_parser", "parse_vk_data"),
        ("parsers.youtube_parser", "parse_youtube_data"),
        ("parsers.keywords", "extract_keywords"),
        ("ai_analyzer.gpt_analyzer", "analyze_speaker_content"),
        ("database.models", "Speaker"),
        ("database.session", "get_session"),
        ("config.settings", "Settings"),
        ("config.topics", "TOPICS"),
        ("utils.formatters", "format_speaker_brief"),
    ]
    
    for module_name, attr in tests:
        try:
            module = __import__(module_name, fromlist=[attr])
            getattr(module, attr)
            print(f"✓ {module_name}.{attr}")
        except Exception as e:
            error_msg = f"✗ {module_name}.{attr}: {e}"
            print(error_msg)
            errors.append(error_msg)
    
    if errors:
        print(f"\n❌ Found {len(errors)} errors")
        return False
    else:
        print(f"\n✅ All imports successful!")
        return True

if __name__ == "__main__":
    import sys
    success = test_imports()
    sys.exit(0 if success else 1)
