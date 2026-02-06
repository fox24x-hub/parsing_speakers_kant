@dataclass
class TopicBrief:
    sport: str
    skill: str
    topic: str
    audience_level: str
    region_priority: str
    format: str
    season: str
    requested_by: int
    extra_notes: str | None = None
