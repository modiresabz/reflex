import reflex as rx

from app.states.home_content_state import HomeContentState


def section_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        label,
        rx.icon("arrow-left", class_name="h-4 w-4"),
        href=href,
        class_name="flex w-fit shrink-0 items-center gap-3 rounded-xl border border-[#ccdfeb] bg-white px-5 py-3 text-sm font-medium text-[#102d4b] transition-colors hover:border-[#4eacd9] hover:text-[#328dbb] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#4eacd9]",
    )


def review_card(
    title: str, name: str, descriptor: str, quote: str
) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.icon("quote", class_name="h-8 w-8 shrink-0 text-[#4eacd9]"),
            rx.el.h3(
                title,
                class_name="text-sm font-semibold leading-7 text-[#377fa4]",
            ),
            class_name="mb-5 flex items-center gap-3",
        ),
        rx.el.blockquote(
            quote, class_name="flex-1 text-sm leading-9 text-[#405a70]"
        ),
        rx.el.div(
            rx.el.span(
                rx.icon("user-round", class_name="h-5 w-5 text-[#4eacd9]"),
                class_name="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[#edf7fc]",
            ),
            rx.el.div(
                rx.el.p(
                    name, class_name="text-base font-semibold text-[#102d4b]"
                ),
                rx.el.p(
                    descriptor,
                    class_name="mt-1 text-xs leading-6 text-[#617487]",
                ),
            ),
            class_name="mt-7 flex items-center gap-3 border-t border-[#e2ecf3] pt-5",
        ),
        class_name="flex h-full flex-col rounded-3xl border border-[#e2ecf3] bg-[#f8fcff] p-6 sm:p-8",
    )


def reviews() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "تجربه همراهان فرزانگان هوشمند",
                        class_name="mb-4 text-sm font-medium text-[#377fa4]",
                    ),
                    rx.el.h2(
                        "نظرات کاربران",
                        id="reviews-heading",
                        class_name="text-2xl font-bold text-[#102d4b] sm:text-3xl",
                    ),
                ),
                section_link(
                    "مشاهده نظرات در سایت اصلی",
                    "https://farzaneganehooshmand.com/",
                ),
                class_name="mb-10 flex flex-col items-start justify-between gap-6 lg:flex-row lg:items-center",
            ),
            rx.el.div(
                review_card(
                    "نظرات مراجعین نوروفیدبک لورتا",
                    "یاشار حسینی",
                    "مراجع روانشناسی کودک",
                    "«من امیر حسینی والد کودک ۸ ساله‌ای با اختلال اضطراب جدایی، به لیلا شقاقی مراجعه کردم. با راهنمایی‌های ایشان و تمرین‌های آرام‌سازی، اضطراب فرزندم به شکل قابل توجهی کاهش یافت و اکنون راحت‌تر به مدرسه می‌رود و شب‌ها آرام می‌خوابد.»",
                ),
                review_card(
                    "تجربه نقشه مغزی",
                    "الهام ر.، سعادت‌آباد",
                    "مراجع نقشه مغزی",
                    "«من برای پسرم که اختلال تمرکز داشت، نقشه مغزی گرفتم. گزارش کامل و دقیق بود و برخورد تیم متخصص بسیار حرفه‌ای. بعد از جلسات نوروفیدبک که با راهنمایی همین مرکز شروع کردیم، تمرکز پسرم به شکل قابل توجهی بهتر شد.»",
                ),
                review_card(
                    "تجربه نوروفیدبک",
                    "محدثه صدیقی",
                    "مراجع نوروفیدبک",
                    "«همسرم بعد از یک سانحه رانندگی دچار اضطراب شدید شده بود. نوروفیدبک کمک کرد تا دوباره کنترل ذهنش رو به دست بگیره. الان هم خودش، هم ما به‌عنوان خانواده کیفیت زندگی‌مون خیلی بهتر شده.»",
                ),
                class_name="grid grid-cols-1 gap-5 lg:grid-cols-3 lg:gap-7",
            ),
            class_name="mx-auto w-full max-w-7xl px-5 py-16 sm:px-8 sm:py-20 lg:px-10",
        ),
        aria_labelledby="reviews-heading",
        class_name="w-full bg-white text-[#102d4b]",
    )


def product_card(title: str, image: str, href: str) -> rx.Component:
    return rx.el.article(
        rx.el.a(
            rx.el.div(
                rx.el.img(
                    src=image,
                    alt=title,
                    loading="lazy",
                    class_name="aspect-[3/2] w-full object-cover transition-transform duration-300 group-hover:scale-105",
                ),
                class_name="overflow-hidden rounded-2xl bg-[#edf7fc]",
            ),
            rx.el.div(
                rx.el.span(
                    "آموزش و رشد فردی",
                    class_name="text-xs font-medium text-[#377fa4]",
                ),
                rx.el.h3(
                    title,
                    class_name="mt-3 flex-1 text-base font-semibold leading-8 text-[#102d4b]",
                ),
                rx.el.div(
                    "مشاهده آموزش",
                    rx.icon("arrow-up-left", class_name="h-4 w-4"),
                    class_name="mt-5 flex items-center justify-between text-sm font-medium text-[#328dbb]",
                ),
                class_name="flex flex-1 flex-col px-2 pb-3 pt-5",
            ),
            href=href,
            class_name="group flex h-full flex-col rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#4eacd9]",
        ),
        class_name="h-full rounded-3xl border border-[#e2ecf3] bg-white p-3 transition-colors hover:border-[#4eacd9]",
    )


def education() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "یادگیری، قدمی برای زندگی بهتر",
                        class_name="mb-4 text-sm font-medium text-[#377fa4]",
                    ),
                    rx.el.h2(
                        "آموزش‌ها و محصولات فرزانگان هوشمند",
                        id="education-heading",
                        class_name="text-2xl font-bold leading-relaxed text-[#102d4b] sm:text-3xl",
                    ),
                ),
                section_link(
                    "همه آموزش‌ها", "https://farzaneganehooshmand.com/shop/"
                ),
                class_name="mb-10 flex flex-col items-start justify-between gap-6 lg:flex-row lg:items-center",
            ),
            rx.el.div(
                product_card(
                    "والدین آگاه، فرزندان سالم",
                    "https://farzaneganehooshmand.com/wp-content/uploads/2025/04/adhd-300x200.jpg",
                    "https://farzaneganehooshmand.com/product/%D9%88%D8%A7%D9%84%D8%AF%DB%8C%D9%86-%D8%A2%DA%AF%D8%A7%D9%87%D8%8C-%D9%81%D8%B1%D8%B2%D9%86%D8%AF%D8%A7%D9%86-%D8%B3%D8%A7%D9%84%D9%85/",
                ),
                product_card(
                    "چگونه انرژی فیزیکی، احساسی، فکری و روانی خود را به دست بیاورید؟",
                    "https://farzaneganehooshmand.com/wp-content/uploads/2024/03/anxiety-girl-300x206.jpg",
                    "https://farzaneganehooshmand.com/product/%D8%A7%D8%B6%D8%B7%D8%B1%D8%A7%D8%A8/",
                ),
                product_card(
                    "کارگاه مهارت‌ها ویژه دانش آموزان",
                    "https://farzaneganehooshmand.com/wp-content/uploads/2024/02/Skills-workshop-for-students-300x240.jpg",
                    "https://farzaneganehooshmand.com/product/%DA%A9%D8%A7%D8%B1%DA%AF%D8%A7%D9%87-%D9%85%D9%87%D8%A7%D8%B1%D8%AA%D9%87%D8%A7-%D9%88%DB%8C%DA%98%D9%87-%D8%AF%D8%A7%D9%86%D8%B4-%D8%A2%D9%85%D9%88%D8%B2%D8%A7%D9%86/",
                ),
                product_card(
                    "تربیت جنسی کودکان و نوجوانان",
                    "https://farzaneganehooshmand.com/wp-content/uploads/2021/09/%D8%A8%D8%B3%D8%AA%D9%87-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-%D8%AA%D8%B1%D8%A8%DB%8C%D8%AA-%D8%AC%D9%86%D8%B3%DB%8C-%DA%A9%D9%88%D8%AF%DA%A9-kid-sexual-safe-education-parents-300x169.jpg",
                    "https://farzaneganehooshmand.com/product/%D8%AA%D8%B1%D8%A8%DB%8C%D8%AA-%D8%AC%D9%86%D8%B3%DB%8C/",
                ),
                class_name="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 lg:gap-6",
            ),
            rx.el.div(
                rx.el.p(
                    "برای آرامش و رشد، یادگیری را از همین امروز آغاز کنید.",
                    class_name="text-base font-medium leading-8 text-[#405a70]",
                ),
                rx.el.a(
                    "شروع رشد و یادگیری",
                    rx.icon("arrow-left", class_name="h-4 w-4"),
                    href="https://farzaneganehooshmand.com/shop/",
                    class_name="flex w-fit items-center gap-3 rounded-xl bg-[#4eacd9] px-6 py-3.5 text-sm font-semibold text-white hover:bg-[#3699c9] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#4eacd9]",
                ),
                class_name="mt-10 flex flex-col items-center justify-center gap-5 text-center sm:flex-row",
            ),
            class_name="mx-auto w-full max-w-7xl px-5 py-16 sm:px-8 sm:py-20 lg:px-10",
        ),
        aria_labelledby="education-heading",
        class_name="w-full bg-[#f2f9fd] text-[#102d4b]",
    )


def article_card(article: dict[str, str]) -> rx.Component:
    return rx.el.article(
        rx.el.a(
            rx.cond(
                article["image"] != "",
                rx.el.img(
                    src=article["image"],
                    alt=article["title"],
                    loading="lazy",
                    class_name="aspect-[16/10] w-full object-cover transition-transform duration-300 group-hover:scale-105",
                ),
                rx.el.div(
                    rx.icon("book-open", class_name="h-12 w-12 text-[#4eacd9]"),
                    class_name="flex aspect-[16/10] w-full items-center justify-center bg-[#edf7fc]",
                ),
            ),
            rx.el.div(
                rx.el.span(
                    "روانشناسی و آگاهی",
                    class_name="text-xs font-medium text-[#377fa4]",
                ),
                rx.el.h3(
                    article["title"],
                    class_name="mt-3 flex-1 text-lg font-semibold leading-8 text-[#102d4b]",
                ),
                rx.el.div(
                    "مطالعه مقاله",
                    rx.icon("arrow-left", class_name="h-4 w-4"),
                    class_name="mt-6 flex items-center justify-between text-sm font-medium text-[#328dbb]",
                ),
                class_name="flex flex-1 flex-col p-6",
            ),
            href=article["href"],
            class_name="group flex h-full flex-col rounded-3xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#4eacd9]",
        ),
        key=article["href"],
        class_name="h-full overflow-hidden rounded-3xl border border-[#e2ecf3] bg-white transition-colors hover:border-[#4eacd9]",
    )


def category_tab(label: str, value: str) -> rx.Component:
    return rx.tabs.trigger(
        label,
        value=value,
        class_name=rx.cond(
            HomeContentState.category == value,
            "!h-auto !rounded-xl !bg-[#4eacd9] !px-5 !py-3 !text-sm !font-semibold !text-white before:!hidden focus-visible:!outline-2 focus-visible:!outline-offset-4 focus-visible:!outline-[#4eacd9]",
            "!h-auto !rounded-xl !bg-[#f2f9fd] !px-5 !py-3 !text-sm !font-medium !text-[#102d4b] before:!hidden hover:!bg-[#e3f3fc] focus-visible:!outline-2 focus-visible:!outline-offset-4 focus-visible:!outline-[#4eacd9]",
        ),
    )


def articles() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "خواندن، آغاز آگاهی است",
                    class_name="mb-4 text-sm font-medium text-[#377fa4]",
                ),
                rx.el.h2(
                    "جدیدترین مقالات روانشناسی برای رشد و آگاهی",
                    id="articles-heading",
                    class_name="text-2xl font-bold leading-relaxed text-[#102d4b] sm:text-3xl",
                ),
                class_name="mb-9 text-center",
            ),
            rx.tabs.root(
                rx.tabs.list(
                    category_tab("مقالات کودک", "child"),
                    category_tab("مقالات نوجوان", "teen"),
                    category_tab("مقالات بزرگسال", "adult"),
                    aria_label="دسته‌بندی مقالات روانشناسی",
                    class_name="!mb-9 !flex !h-auto !flex-wrap !justify-center !gap-3 !bg-white !p-1 !shadow-none",
                ),
                rx.tabs.content(
                    rx.el.div(
                        rx.foreach(
                            HomeContentState.child_articles, article_card
                        ),
                        class_name="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3",
                    ),
                    value="child",
                    class_name="!mt-0 focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
                ),
                rx.tabs.content(
                    rx.el.div(
                        rx.foreach(
                            HomeContentState.teen_articles, article_card
                        ),
                        class_name="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3",
                    ),
                    value="teen",
                    class_name="!mt-0 focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
                ),
                rx.tabs.content(
                    rx.el.div(
                        rx.foreach(
                            HomeContentState.adult_articles, article_card
                        ),
                        class_name="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3",
                    ),
                    value="adult",
                    class_name="!mt-0 focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
                ),
                value=HomeContentState.category,
                on_change=HomeContentState.select_category,
                dir="rtl",
                class_name="w-full text-[#102d4b]",
            ),
            rx.el.div(
                section_link(
                    "مقالات بیشتر", "https://farzaneganehooshmand.com/blog/"
                ),
                class_name="mt-10 flex justify-center",
            ),
            class_name="mx-auto w-full max-w-7xl px-5 py-16 sm:px-8 sm:py-20 lg:px-10",
        ),
        aria_labelledby="articles-heading",
        class_name="w-full bg-white text-[#102d4b]",
    )
