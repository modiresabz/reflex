import reflex as rx

from app.components.header import header
from app.components.home_sections import books, hero, services
from app.components.learning_sections import articles, education, reviews
from app.components.footer import footer
from app.states.navigation_state import NavigationState


def index() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.main(
            hero(),
            services(),
            books(),
            reviews(),
            education(),
            articles(),
            class_name="w-full min-w-0 bg-white text-[#102d4b]",
        ),
        footer(),
        dir="rtl",
        lang="fa",
        class_name="min-h-dvh w-full bg-white font-['Vazirmatn'] text-[#102d4b] antialiased",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            cross_origin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index,
    route="/",
    title="لیلا شقاقی | فرزانگان هوشمند",
    description="معرفی لیلا شقاقی، خدمات روانشناسی فرزانگان هوشمند و کتاب‌های روانشناسی و توسعه فردی.",
    on_load=NavigationState.close_menu,
)
