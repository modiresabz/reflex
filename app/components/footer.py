import reflex as rx


def footer_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon("chevron-left", class_name="h-3.5 w-3.5 text-[#4eacd9]"),
        label,
        href=href,
        class_name="flex w-fit items-center gap-2 rounded-lg py-2 text-sm text-[#405a70] transition-colors hover:text-[#328dbb] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#4eacd9]",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.el.img(
                            src="https://farzaneganehooshmand.com/wp-content/uploads/2026/07/farzaneganehooshmand-2026-logo-300x124.png",
                            alt="فرزانگان هوشمند",
                            width=300,
                            height=124,
                            loading="lazy",
                            class_name="h-auto w-44 object-contain",
                        ),
                        href="https://farzaneganehooshmand.com/",
                        aria_label="صفحه اصلی فرزانگان هوشمند",
                        class_name="block w-fit rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#4eacd9]",
                    ),
                    rx.el.h2(
                        "مرکز مشاوره و روانشناسی فرزانگان هوشمند",
                        class_name="mt-6 text-base font-semibold leading-8 text-[#102d4b]",
                    ),
                    rx.el.p(
                        "مرکز «فرزانگان هوشمند» با هدف ارتقای سلامت روان، رشد شناختی و بهبود کیفیت زندگی افراد فعالیت می‌کند.",
                        class_name="mt-3 text-sm leading-8 text-[#617487]",
                    ),
                    class_name="min-w-0 lg:col-span-2",
                ),
                rx.el.nav(
                    rx.el.h2(
                        "دسترسی سریع",
                        class_name="mb-4 text-lg font-semibold text-[#102d4b]",
                    ),
                    footer_link("خانه", "https://farzaneganehooshmand.com/"),
                    footer_link(
                        "درباره ما",
                        "https://farzaneganehooshmand.com/about-us/",
                    ),
                    footer_link(
                        "تماس با ما",
                        "https://farzaneganehooshmand.com/contact-us/",
                    ),
                    footer_link(
                        "مقالات", "https://farzaneganehooshmand.com/blog/"
                    ),
                    footer_link(
                        "آموزش‌ها و محصولات",
                        "https://farzaneganehooshmand.com/shop/",
                    ),
                    aria_label="پیوندهای پابرگ",
                    class_name="flex flex-col items-start",
                ),
                rx.el.div(
                    rx.el.h2(
                        "ارتباط با ما",
                        class_name="mb-4 text-lg font-semibold text-[#102d4b]",
                    ),
                    rx.el.ul(
                        rx.el.li(
                            "تلفن: ",
                            rx.el.span("۰۲۱۸۸۱۹۴۲۰۷", dir="ltr"),
                            class_name="break-words text-sm leading-8 text-[#405a70]",
                        ),
                        rx.el.li(
                            "موبایل: ",
                            rx.el.span("۰۹۱۲۸۳۸۱۷۹۵", dir="ltr"),
                            class_name="break-words text-sm leading-8 text-[#405a70]",
                        ),
                        rx.el.li(
                            "نشانی: سعادت آباد بلوار دریا بین موج و گلها پلاک ۴ واحد ۳",
                            class_name="break-words text-sm leading-8 text-[#405a70]",
                        ),
                        class_name="flex flex-col gap-3",
                    ),
                    rx.el.div(
                        footer_link(
                            "صفحه تماس با مرکز",
                            "https://farzaneganehooshmand.com/contact-us/",
                        ),
                        class_name="mt-4",
                    ),
                    class_name="min-w-0",
                ),
                class_name="grid grid-cols-1 gap-10 sm:grid-cols-2 lg:grid-cols-4 lg:gap-12",
            ),
            rx.el.div(
                rx.el.p(
                    "تمامی حقوق برای فرزانگان هوشمند محفوظ است.",
                    class_name="text-xs leading-7 text-[#617487]",
                ),
                rx.el.span(
                    rx.icon(
                        "heart-handshake", class_name="h-4 w-4 text-[#4eacd9]"
                    ),
                    "همراه شما در مسیر آرامش و رشد",
                    class_name="flex items-center gap-2 text-xs leading-7 text-[#617487]",
                ),
                class_name="mt-12 flex flex-col items-start justify-between gap-3 border-t border-[#dcebf4] pt-6 sm:flex-row sm:items-center",
            ),
            class_name="mx-auto w-full max-w-7xl px-5 pb-7 pt-14 sm:px-8 sm:pt-16 lg:px-10",
        ),
        class_name="w-full border-t border-[#e2ecf3] bg-[#f2f9fd] text-[#102d4b]",
    )
