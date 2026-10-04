import reflex as rx

from urllib.parse import quote


DOMAIN = "https://farzaneganehooshmand.com"


def source_article(category: str, slug: str, title: str) -> dict[str, str]:
    return {
        "category": category,
        "title": title,
        "href": f"{DOMAIN}/{quote(slug, safe='-')}/",
        "image": "",
    }


class HomeContentState(rx.State):
    category: str = "child"
    articles: list[dict[str, str]] = [
        source_article(
            "child",
            "child-play-therapy-guide",
            "بازی درمانی کودکان؛ راهنمای جامع والدین برای درمان اضطراب، بیش فعالی و مشکلات رفتاری",
        ),
        source_article(
            "child",
            "why-knowledge-alone-is-not-enough",
            "چرا یادگیری مهارت‌های فردی در کنار دانش تحصیلی برای کودکان ضروری است؟",
        ),
        source_article(
            "child",
            "back-to-school-kids",
            "شروع سال تحصیلی برای کودکان؛ چگونه در کنار فرزندمان باشیم، بدون اینکه جای او زندگی کنیم؟",
        ),
        source_article(
            "child",
            "life-skills-education-elementary-children",
            "چرا آموزش مهارت‌های زندگی به کودکان دبستانی ضروری است؟",
        ),
        source_article(
            "teen",
            "professional-academic-consulting",
            "مشاوره تحصیلی حرفه‌ای برای موفقیت در کنکور: برنامه‌ریزی، پشتیبانی، استعدادیابی و آرامش ذهنی",
        ),
        source_article(
            "teen",
            "what-girls-should-know-about-sexual-health",
            "آنچه دختران درباره مسائل جنسی باید بدانند",
        ),
        source_article(
            "teen", "پیام-مشاور-مدرسه-به-والدین", "پیام مشاور مدرسه به والدین"
        ),
        source_article(
            "adult",
            "neurofeedback-therapy",
            "نوروفیدبک چیست؟ کاربردها، مزایا و درمان قطعی اختلالات روان",
        ),
        source_article(
            "adult", "neuroscience-brain-mapping", "نقشه مغزی چیست؟"
        ),
        source_article("adult", "حسرت-های-والدین", "حسرت‌ های والدین"),
        source_article("adult", "حفظ-و-تداوم-روابط", "حفظ و تداوم روابط"),
    ]

    @rx.var
    def child_articles(self) -> list[dict[str, str]]:
        return [
            article
            for article in self.articles
            if article["category"] == "child"
        ]

    @rx.var
    def teen_articles(self) -> list[dict[str, str]]:
        return [
            article
            for article in self.articles
            if article["category"] == "teen"
        ]

    @rx.var
    def adult_articles(self) -> list[dict[str, str]]:
        return [
            article
            for article in self.articles
            if article["category"] == "adult"
        ]

    @rx.event
    def select_category(self, value: str):
        if value in {"child", "teen", "adult"}:
            self.category = value
