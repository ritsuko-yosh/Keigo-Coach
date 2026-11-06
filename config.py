"""
config.py - Keigo Coach: single source of truth for all settings.
All file paths, enum values, display labels, colors, UI text, and CSS
class names live here. Python files import from this module only.
"""

# ── File paths ────────────────────────────────────────────────────────────────

CSV_PATH              = "data/phrases.csv"
SCENARIOS_CSV_PATH    = "data/scenarios.csv"
CSS_PATH              = "assets/style.css"
BELLE_SVG_PATH        = "assets/belle_sit.svg"
BELLE_POSES_CSS_PATH  = "assets/belle_poses.css"
ABOUT_MD_PATH         = "content/about.md"
HOME_MD_PATH          = "content/home.md"

# ── Theme colors (also defined as CSS variables in assets/style.css) ──────────

COLOR_BG           = "#FAF6EE"
COLOR_TEXT         = "#2F2A26"
COLOR_TEXT_MUTED   = "#6E6660"
COLOR_CARD         = "#FFFFFF"
COLOR_ACCENT       = "#E86A5F"
COLOR_WASHI        = "#F3D27A"

COLOR_SONKEIGO  = "#9CC5E3"
COLOR_KENJOGO1  = "#A8C3A0"
COLOR_KENJOGO2  = "#C9B8E8"
COLOR_TEINEIGO  = "#F6C9A8"
COLOR_BIKAGO    = "#F2B8C6"

# ── Belle pose class names (must match belle_poses.css exactly) ───────────────

BELLE_POSES = {
    "default":       "pose-sit",
    "correct_steps": "pose-bow-small",
    "correct_keigo": "pose-bow-deep",
    "wrong":         "pose-tilt",
}

BELLE_COMMENTS = {
    "pose-sit":       "",
    "pose-bow-small": "うん。",
    "pose-bow-deep":  "正解です。",
    "pose-tilt":      "あれ…？",
}

# ── Column definitions ────────────────────────────────────────────────────────

PHRASE_COLUMNS = [
    "id", "situation", "action_by", "casual_jp", "polite_jp", "keigo_jp",
    "keigo_type", "english_meaning", "explanation_rule", "explanation_example",
    "source", "source_url", "source_page", "verified",
]

SCENARIO_COLUMNS = [
    "id", "situation", "scene_en", "scene_jp", "actor", "listener",
    "correct_type", "correct_sentence", "wrong_options", "explanation_en",
    "source", "source_url", "source_page", "verified",
]

# ── Allowed enum values ───────────────────────────────────────────────────────

SITUATIONS        = ["interview", "email", "phone", "meeting"]
ACTION_BY_VALUES  = ["me", "other_person"]
KEIGO_TYPES       = ["尊敬語", "謙譲語I", "謙譲語II", "丁寧語", "美化語"]

SCENARIO_SITUATIONS = [
    "recorded_interview", "recruiter_email", "talking_about_my_school",
    "phone_call", "career_fair",
]
ACTOR_VALUES    = ["me", "my_boss", "client", "client_boss", "interviewer"]
LISTENER_VALUES = ["insider", "outsider"]

# ── Navigation ────────────────────────────────────────────────────────────────

NAV_HOME           = "Home"
NAV_PRACTICE       = "Practice"
NAV_PHRASE_LIBRARY = "Phrase Library"
NAV_MY_PROGRESS    = "My Progress"
NAV_ABOUT          = "About"

NAV_PAGES = [
    ("pages/home.py",           NAV_HOME),
    ("pages/practice.py",       NAV_PRACTICE),
    ("pages/phrase_library.py", NAV_PHRASE_LIBRARY),
    ("pages/my_progress.py",    NAV_MY_PROGRESS),
    ("pages/about.py",          NAV_ABOUT),
]

# ── Actor display (step 1) ────────────────────────────────────────────────────

ACTOR_STEP_MAPPING = {
    "me":           "me",
    "my_boss":      "my_boss",
    "client":       "other",
    "client_boss":  "other",
    "interviewer":  "other",
}

ACTOR_STEP_OPTIONS = {
    "me":      "I am doing it",
    "my_boss": "My boss or colleague (part of my group, ウチ) is doing it",
    "other":   "The interviewer, recruiter, or client (ソト) is doing it",
}

# ── Listener display (step 2) ─────────────────────────────────────────────────

LISTENER_OPTIONS = {
    "insider":  "Someone inside my group (ウチ), such as a boss, colleague, or classmate",
    "outsider": "Someone outside my group (ソト), such as a recruiter, client, or interviewer",
}

# ── Step labels and hints ─────────────────────────────────────────────────────

STEP_LABELS = {
    1: "Who performs the action in this scene?",
    2: "Who is the listener?",
    3: "Which type of keigo fits this situation?",
    4: "Pick the correct sentence.",
}

STEP_HINTS = {
    1: "The keigo choice depends on who performs the main action.",
    2: "ウチ (in-group) or ソト (out-group): this determines whether to honor or humble.",
    3: "尊敬語 honors the other person's actions. 謙譲語 lowers your own or your group's.",
    4: "Match the verb transformation to the keigo type you identified in Step 3.",
}

PROGRESS_FORMAT = "Scenario {scenario} of {total},  Step {step} of {total_steps}"

# ── Feedback messages ─────────────────────────────────────────────────────────

FEEDBACK_CORRECT = {
    1: "Right.",
    2: "Right. This person is outside your group (ソト), so you lower your language to them.",
    3: "Right. {type} is the appropriate choice here.",
    4: "That's the right form.",
}

FEEDBACK_WRONG = {
    1: "Not quite. The action here is by {correct_actor}.",
    2: "Actually, this listener is outside your group (ソト). That matters for which forms to use.",
    3: "Not quite. The right type here is {correct_type}.",
    4: "The correct sentence is: {correct_sentence}",
}

# ── Home page ─────────────────────────────────────────────────────────────────

START_BUTTON_LABEL        = "Start practicing"
HOME_SECTION_HOW          = "How it works"
HOME_SECTION_SITUATIONS   = "Choose a situation"

SHOWING_FORMAT = "Showing {shown} of {total} phrases"

SITUATION_CARDS = [
    ("recorded_interview",      "Recorded Interview"),
    ("recruiter_email",         "Recruiter Email"),
    ("talking_about_my_school", "Talking About My School"),
    ("phone_call",              "Phone Call"),
    ("career_fair",             "Career Fair"),
]

# ── My Progress page ──────────────────────────────────────────────────────────

MY_PROGRESS_COMING_SOON = "Progress tracking is coming soon."

# ── UI text ───────────────────────────────────────────────────────────────────

APP_TITLE    = "Keigo Coach"
APP_SUBTITLE = "Step-by-step keigo practice for bilingual job seekers"

SIMULATOR_PAGE_TITLE  = "Practice"
LIBRARY_PAGE_TITLE    = "Phrase Library"
ABOUT_PAGE_TITLE      = "About"
HOME_PAGE_TITLE       = "Home"
PROGRESS_PAGE_TITLE   = "My Progress"

NAV_PREV_LABEL           = "Previous"
NAV_NEXT_LABEL           = "Next scenario"
ALL_SCENARIOS_COMPLETE   = "You have finished all scenarios."
SOURCE_NEEDED_LABEL      = "Source needed"
UNVERIFIED_LABEL         = "Unverified"
NO_RESULTS_MESSAGE       = "No phrases match the current filters."

ICON_CORRECT = "+"
ICON_WRONG   = "x"

FILTER_HEADING         = "Filters"
FILTER_SITUATION_LABEL = "Situation"
FILTER_KEIGO_LABEL     = "Keigo Type"
HIDE_KEIGO_LABEL       = "Hide keigo (test yourself)"

# ── Phrase library labels ─────────────────────────────────────────────────────

ACTION_BY_LABELS = {
    "me":           ("you", "You are the speaker"),
    "other_person": ("them", "The other person speaks"),
}

SITUATION_LABELS = {
    "interview": "Interview",
    "email":     "Email",
    "phone":     "Phone",
    "meeting":   "Meeting",
}

# ── Badge CSS classes per keigo type ──────────────────────────────────────────

KEIGO_TYPE_CSS = {
    "尊敬語":  "kc-badge-sonkeigo",
    "謙譲語I": "kc-badge-kenjogo1",
    "謙譲語II":"kc-badge-kenjogo2",
    "丁寧語":  "kc-badge-teineigo",
    "美化語":  "kc-badge-bikago",
}
