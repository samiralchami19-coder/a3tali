# أعطالي (a3tali.com)

- `site/` ملفات الموقع الجاهزة. هذا ما تنشره Cloudflare.
- `source/` مصدر الموقع: بيانات الرموز في `data/`، و`build.py` يبني الجدول، و`gen_site.py` يولّد صفحات `site/`.
- `wrangler.jsonc` يخبر Cloudflare أن ملفات الموقع في `site/`.
