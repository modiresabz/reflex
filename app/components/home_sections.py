import reflex as rx


def intro_fact(icon: str, text: str) -> rx.Component:
    return rx.el.li(
        rx.el.span(
            rx.icon(icon, class_name="h-5 w-5 text-[#4eacd9]"),
            class_name="mt-0.5 flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-white",
        ),
        rx.el.span(
            text, class_name="text-sm leading-8 text-[#405a70] sm:text-base"
        ),
        class_name="flex items-start gap-3",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(class_name="h-2 w-2 rounded-full bg-[#4eacd9]"),
                    "مرکز مشاوره و روانشناسی فرزانگان هوشمند",
                    class_name="mb-6 flex items-center gap-2 text-xs font-medium text-[#377fa4] sm:text-sm",
                ),
                rx.el.h1(
                    "لیلا شقاقی",
                    class_name="text-5xl font-bold leading-tight text-[#102d4b] sm:text-6xl lg:text-7xl",
                ),
                rx.el.p(
                    "مدیرمجموعه روانشناسی فرزانگان هوشمند",
                    class_name="mt-5 text-base font-medium leading-8 text-[#102d4b] sm:text-lg",
                ),
                rx.el.div(class_name="my-7 h-1 w-16 rounded-full bg-[#4eacd9]"),
                rx.el.ul(
                    intro_fact(
                        "book-open",
                        "مولف 7 کتاب در زمینه روانشناسی و توسعه فردی",
                    ),
                    intro_fact("award", "بیش از 20 سال تجربه روانشناسی حرفه‌ای"),
                    intro_fact(
                        "heart-handshake",
                        "هزاران تجربه موفق درمان اضطراب، افسردگی، اختلالات یادگیری و ...",
                    ),
                    intro_fact(
                        "presentation",
                        "برگزاری صدها سمینار، سخنرانی، وبینار ، کارگاه و ...",
                    ),
                    class_name="flex flex-col gap-4",
                ),
                rx.el.div(
                    rx.el.a(
                        "ارتباط با مرکز مشاوره",
                        rx.icon("arrow-up-left", class_name="h-4 w-4"),
                        href="https://farzaneganehooshmand.com/contact-us/",
                        class_name="flex w-fit items-center gap-3 rounded-xl bg-[#4eacd9] px-5 py-3.5 text-sm font-semibold text-white transition-colors hover:bg-[#3699c9] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#4eacd9]",
                    ),
                    rx.el.a(
                        "بیشتر درباره ما",
                        rx.icon("arrow-left", class_name="h-4 w-4"),
                        href="https://farzaneganehooshmand.com/about-us/",
                        class_name="flex w-fit items-center gap-2 rounded-xl px-3 py-3.5 text-sm font-medium text-[#102d4b] transition-colors hover:bg-white focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
                    ),
                    class_name="mt-8 flex flex-wrap items-center gap-3",
                ),
                class_name="min-w-0 lg:py-8",
            ),
            rx.el.div(
                rx.el.img(
                    src="https://farzaneganehooshmand.com/wp-content/uploads/2026/07/main-farzanegnehooshmand-banner.webp",
                    alt="لیلا شقاقی، مدیر مجموعه روانشناسی فرزانگان هوشمند",
                    fetch_priority="high",
                    class_name="h-auto max-h-[580px] w-full object-contain",
                ),
                class_name="flex min-w-0 items-center justify-center overflow-hidden rounded-[2rem] bg-[#eaf5fc] p-3 sm:p-5 lg:p-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-center gap-10 px-5 py-12 sm:px-8 sm:py-16 lg:grid-cols-2 lg:gap-14 lg:px-10 lg:py-16",
        ),
        aria_label="معرفی لیلا شقاقی",
        class_name="w-full bg-[#f2f9fd]",
    )


def service_card(
    title: str, description: str, icon: str, href: str, number: str
) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, class_name="h-8 w-8 text-[#4eacd9]"),
                class_name="flex h-16 w-16 items-center justify-center rounded-2xl border border-[#deedf5] bg-[#edf7fc]",
            ),
            rx.el.span(number, class_name="text-sm font-medium text-[#a3bdcd]"),
            class_name="mb-7 flex items-center justify-between",
        ),
        rx.el.h3(title, class_name="text-xl font-bold text-[#102d4b]"),
        rx.el.p(
            description,
            class_name="mb-7 mt-4 flex-1 text-sm leading-8 text-[#617487] sm:text-base",
        ),
        rx.el.a(
            "آشنایی با خدمات",
            rx.icon(
                "arrow-left",
                class_name="h-4 w-4 transition-transform group-hover:-translate-x-1",
            ),
            href=href,
            class_name="group flex w-fit items-center gap-3 rounded-lg text-sm font-semibold text-[#328dbb] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#4eacd9]",
        ),
        class_name="flex h-full flex-col rounded-3xl border border-[#e1ecf3] bg-white p-7 transition-colors hover:border-[#4eacd9] sm:p-8",
    )


def services() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(class_name="h-px w-8 bg-[#4eacd9]"),
                    rx.el.span(
                        "همراه شما در مسیر سلامت روان",
                        class_name="text-sm font-medium text-[#377fa4]",
                    ),
                    class_name="mb-4 flex items-center justify-center gap-3",
                ),
                rx.el.h2(
                    "معرفی خدمات فرزانگان هوشمند",
                    class_name="text-2xl font-bold leading-relaxed text-[#102d4b] sm:text-3xl",
                ),
                class_name="mb-10 text-center sm:mb-12",
            ),
            rx.el.div(
                service_card(
                    "بازی درمانی",
                    "راهی مؤثر برای کاهش اضطراب کودکان و تقویت مهارت‌های ارتباطی از طریق بازی هدایت‌شده.",
                    "blocks",
                    "https://farzaneganehooshmand.com/child-play-therapy-services/",
                    "۰۱",
                ),
                service_card(
                    "نقشه مغزی",
                    "ابزاری تخصصی برای بررسی امواج مغزی و طراحی مسیر درمانی دقیق‌تر است.",
                    "brain",
                    "https://farzaneganehooshmand.com/brain-mapping-qeeg-services/",
                    "۰۲",
                ),
                service_card(
                    "نوروفیدبک لورتا",
                    "روشی پیشرفته برای آموزش مغز که به بهبود تمرکز، آرامش و عملکرد ذهنی کمک می‌کند.",
                    "activity",
                    "https://farzaneganehooshmand.com/loretta-neurofeedback-technology-to-improve-your-childs-brain/",
                    "۰۳",
                ),
                class_name="grid grid-cols-1 gap-5 md:grid-cols-3 lg:gap-7",
            ),
            class_name="mx-auto w-full max-w-7xl px-5 py-16 sm:px-8 sm:py-20 lg:px-10",
        ),
        aria_label="خدمات فرزانگان هوشمند",
        class_name="w-full bg-white",
    )


def book_card(title: str, filename: str, href: str) -> rx.Component:
    return rx.el.article(
        rx.el.a(
            rx.el.div(
                rx.el.img(
                    src=f"https://farzaneganehooshmand.com/wp-content/uploads/elementor/thumbs/{filename}",
                    alt=title,
                    loading="lazy",
                    class_name="h-52 w-full object-contain transition-transform duration-300 group-hover:scale-105 sm:h-64",
                ),
                class_name="flex items-center justify-center rounded-2xl bg-[#f2f7fa] px-4 py-7 sm:px-6",
            ),
            rx.el.div(
                rx.el.h3(
                    title,
                    class_name="min-h-14 text-sm font-semibold leading-7 text-[#102d4b] sm:text-base",
                ),
                rx.el.div(
                    rx.el.span("مشاهده کتاب"),
                    rx.icon("arrow-up-left", class_name="h-4 w-4"),
                    class_name="mt-4 flex items-center justify-between text-xs font-medium text-[#328dbb] sm:text-sm",
                ),
                class_name="px-2 pb-2 pt-5",
            ),
            href=href,
            class_name="group block h-full rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#4eacd9]",
        ),
        class_name="h-full rounded-3xl border border-[#e2ecf3] bg-white p-3 transition-colors hover:border-[#4eacd9] sm:p-4",
    )


def books() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("book-open", class_name="h-5 w-5"),
                        "برای آرامش، برای رشد",
                        class_name="mb-4 flex items-center gap-2 text-sm font-medium text-[#377fa4]",
                    ),
                    rx.el.h2(
                        "معرفی کتابهای لیلا شقاقی",
                        class_name="text-2xl font-bold leading-relaxed text-[#102d4b] sm:text-3xl",
                    ),
                    rx.el.p(
                        "همین امروز قدمی به سوی آرامش و رشد فردی بردارید!",
                        class_name="mt-4 text-base font-medium leading-8 text-[#405a70]",
                    ),
                    class_name="min-w-0",
                ),
                rx.el.a(
                    "مشاهده همه کتاب‌ها",
                    rx.icon("arrow-left", class_name="h-4 w-4"),
                    href="https://farzaneganehooshmand.com/shop/",
                    class_name="flex w-fit shrink-0 items-center gap-3 rounded-xl border border-[#ccdfeb] bg-white px-5 py-3 text-sm font-medium text-[#102d4b] transition-colors hover:border-[#4eacd9] hover:text-[#328dbb] focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
                ),
                class_name="mb-10 flex flex-col items-start justify-between gap-6 lg:flex-row lg:items-center",
            ),
            rx.el.div(
                book_card(
                    "شفای زخم‌های درون",
                    "The-Psychology-of-Healing-Inner-Wounds-Book-rdumxwdrjuu78tst6q8eir5laudw7npzq002flj05k.jpg",
                    "https://farzaneganehooshmand.com/product/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B4%D9%81%D8%A7%DB%8C-%D8%B2%D8%AE%D9%85-%D9%87%D8%A7%DB%8C-%D8%AF%D8%B1%D9%88%D9%86/",
                ),
                book_card(
                    "۸ گام مؤثر در تربیت فرزندان",
                    "book-8-effective-steps-for-raising-children-rcp4q9ik5e58o95gjzxztvwd8mibm8nq24ily2x6dk.jpg",
                    "https://farzaneganehooshmand.com/shop/",
                ),
                book_card(
                    "معلم مرجع",
                    "Reference-teacher-book-rcp4q7mvrq2o1186uz4qowdg1url6ug9dv7mzizyq0.jpg",
                    "https://farzaneganehooshmand.com/shop/",
                ),
                book_card(
                    "فتح قله فرزندپروری",
                    "Conquering-the-Peak-of-Child-Rearing-book-rcp4q6p1kw1dpf9k0gq44elzggw7z5cj1qk5i91cw8.jpg",
                    "https://farzaneganehooshmand.com/shop/",
                ),
                class_name="grid grid-cols-1 gap-5 min-[400px]:grid-cols-2 lg:grid-cols-4 lg:gap-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("package", class_name="h-6 w-6 text-[#4eacd9]"),
                    class_name="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-[#edf7fc]",
                ),
                rx.el.p(
                    "برای سفارش ، با مرکز مشاوره فرزانگان هوشمند تماس بگیرید و کتاب‌ها را به‌راحتی و از طریق پست دریافت کنید. فرصت را از دست ندهید و مطالعه‌ای متفاوت را آغاز کنید!",
                    class_name="flex-1 text-sm leading-8 text-[#617487]",
                ),
                rx.el.a(
                    "تماس با مرکز",
                    rx.icon("arrow-up-left", class_name="h-4 w-4"),
                    href="https://farzaneganehooshmand.com/contact-us/",
                    class_name="flex w-fit shrink-0 items-center gap-2 rounded-lg px-2 py-2 text-sm font-semibold text-[#328dbb] hover:bg-[#edf7fc] focus-visible:outline-2 focus-visible:outline-[#4eacd9]",
                ),
                class_name="mt-8 flex flex-col items-start gap-4 rounded-2xl border border-[#e2ecf3] bg-white p-5 sm:flex-row sm:items-center sm:p-6",
            ),
            class_name="mx-auto w-full max-w-7xl px-5 py-16 sm:px-8 sm:py-20 lg:px-10",
        ),
        aria_label="کتابهای لیلا شقاقی",
        class_name="w-full bg-[#f2f9fd]",
    )
