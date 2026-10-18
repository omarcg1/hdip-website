#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HDIP site content, English and Arabic.

Every figure and every paragraph here comes from the 2024 source documents
supplied by HDIP (see SOURCES below). Nothing is invented. Where the approved
site structure asks for content we do not have, the gap is recorded in
GAPS and rendered as a visible "content needed" note rather than filled in.
"""

SOURCES = {
    "profile":      "تعريف.docx — organisation profile, vision, mission, 15 objectives (AR)",
    "directions":   "توجهات البرنامج الإعلامي.docx — Strategic Directions 2024 (AR + EN)",
    "activities":   "الأنشطة المنفذة في عام 2024.docx — Activities Implemented 2024 (AR + EN)",
    "outputs":      "أبرز المخرجات لعام 2024.docx — Key Outputs 2024 (AR + EN)",
    "recs":         "التوصيات.docx — Recommendations 2024 (AR + EN)",
    "rte":          "مشروع الحق في التعليم.docx — Right to Education 2024 (AR + EN)",
    "women_able":   "مشروع نساء قادرات على تغيير المجتمع.docx — Women Able 2020–2024 (AR)",
    "women_lead":   "مشروع نساء قياديات في المجالس المحلية.docx — Women Leaders (AR + EN)",
    "youth":        "مشروع تعزيز القيادات الشابة في الجامعات.docx — Youth Leadership (AR + EN)",
    "photo":        "صورة جماعية.docx — closing conference group photograph",
}

# Content the approved structure requires and the 2024 batch does not supply.
GAPS = {
    "en": [
        ("About — Our Approach", "No source document. The approved structure lists it as an About section."),
        ("About — Why Partner With Us (7 principles)", "No source document; the English HDIP profile was not supplied."),
        ("About — Team & Board", "Names, roles and photographs not supplied."),
        ("Impact in numbers — 2025 figures", "The 2025 documents were not supplied, so the year switch shows 2024 only."),
        ("Annual Reports 2022, 2023, 2025", "Only the 2024 batch was supplied."),
        ("Research, Policy & Knowledge — full source", "Main source is the 2022 Narrative Report, not supplied; this page is built from the 2024 research pillar only."),
        ("Women Able to Change Society — English text", "The English half of that document contains Right to Education text instead."),
        ("Donors and partners", "Only two are visible in the supplied photographs; no list or logos were supplied."),
        ("Annual report PDFs", "Not supplied, so report pages have no download."),
        ("Contact details", "Address, phone, email and social links need confirmation."),
    ],
    "ar": [
        ("نبذة عنا — منهجيتنا", "لا يوجد مستند مصدر. الهيكل المعتمد يدرجه ضمن صفحة «عن البرنامج»."),
        ("نبذة عنا — لماذا الشراكة معنا (٧ مبادئ)", "لا يوجد مستند مصدر؛ لم يتم تزويدنا بالملف التعريفي بالإنجليزية."),
        ("نبذة عنا — الفريق ومجلس الإدارة", "لم يتم تزويدنا بالأسماء والمهام والصور."),
        ("الأثر بالأرقام — أرقام 2025", "لم يتم تزويدنا بمستندات 2025، لذلك يعرض المبدّل عام 2024 فقط."),
        ("التقارير السنوية 2022 و2023 و2025", "لم يتم تزويدنا إلا بمستندات عام 2024."),
        ("البحث والسياسات والمعرفة — المصدر الكامل", "المصدر الأساسي هو التقرير السردي 2022 ولم يتم تزويدنا به."),
        ("نساء قادرات على تغيير المجتمع — النص الإنجليزي", "القسم الإنجليزي في الملف يحتوي نص مشروع الحق في التعليم."),
        ("الممولون والشركاء", "لم يظهر سوى شريكين في الصور المرفقة، ولم تُزوَّد قائمة أو شعارات."),
        ("ملفات التقارير السنوية PDF", "لم يتم تزويدنا بها، لذلك لا يوجد تنزيل في صفحات التقارير."),
        ("بيانات الاتصال", "العنوان والهاتف والبريد وروابط التواصل بحاجة إلى تأكيد."),
    ],
}

GOVERNORATES = ["Hebron", "Bethlehem", "Abu Dis", "Ramallah", "Jenin", "Tulkarm", "Nablus", "Gaza"]
GOVERNORATES_AR = ["الخليل", "بيت لحم", "أبو ديس", "رام الله", "جنين", "طولكرم", "نابلس", "غزة"]

# --------------------------------------------------------------------------
# Shared figures — all from the 2024 documents
# --------------------------------------------------------------------------
IMPACT_2024 = [
    dict(num="345",   label_en="activities delivered by the Right to Education Project",
         label_ar="نشاطًا نفّذه مشروع الحق في التعليم"),
    dict(num="8,321", label_en="participants reached, 61% of them female",
         label_ar="مستفيدًا ومستفيدة، 61% منهم إناث"),
    dict(num="85",    label_en="first aid courses for 1,700 school and university students",
         label_ar="دورة إسعاف أولي استفاد منها 1,700 طالب وطالبة"),
    dict(num="355",   label_en="participants with disabilities included across the programme",
         label_ar="مشاركًا من ذوي الإعاقة ضمن أنشطة البرنامج"),
]

NAV = {
    "en": [("about.html", "About"), ("work.html", "Our Work"), ("projects.html", "Projects"),
           ("reports.html", "Reports"), ("news.html", "News & Stories")],
    "ar": [("about.html", "عن البرنامج"), ("work.html", "مجالات عملنا"), ("projects.html", "المشاريع"),
           ("reports.html", "التقارير"), ("news.html", "أخبار وقصص")],
}

UI = {
    "en": dict(
        lang_label="العربية", lang_href_note="Arabic", dir="ltr", code="en",
        org="Health Development Information and Policy Institute",
        org_short="HDIP", place="Ramallah · Palestine",
        contact="Contact us", partner="Partner with us", skip="Skip to content",
        home="Home", explore="Explore", read_more="Read more", all_news="All news",
        back_work="All programme areas", back_projects="All projects",
        at_a_glance="At a glance", objectives="Objectives", activities="Activities and outputs",
        results="Results", related_projects="Related projects", related_news="Related news",
        key_figures="Key figures", governorates="Governorates", target_group="Target group",
        years_label="Years",
        today="Today",
        participants="Participants", partner_label="Partner", status="Status",
        years="Years", ongoing="Ongoing", completed="Completed", content_needed="Content needed",
        content_needed_note="This section is part of the approved structure. HDIP has not yet supplied the source material.",
        credits="Photography & credits", sources="Sources",
        download="Download PDF", no_download="PDF not yet supplied",
        year_switch="Year", female="female", male="male", pwd="with disabilities",
        footer_about="An independent, non-profit Palestinian institute for research, advocacy and capacity building in health, education and development — since 1989.",
        developed_by="Developed by",
    ),
    "ar": dict(
        lang_label="English", lang_href_note="English", dir="rtl", code="ar",
        org="البرنامج الإعلامي للتطوير الصحي",
        org_short="HDIP", place="رام الله · فلسطين",
        contact="اتصل بنا", partner="كن شريكًا", skip="تخطَّ إلى المحتوى",
        home="الرئيسية", explore="تصفّح", read_more="اقرأ المزيد", all_news="كل الأخبار",
        back_work="كل مجالات العمل", back_projects="كل المشاريع",
        at_a_glance="لمحة سريعة", objectives="الأهداف", activities="الأنشطة والمخرجات",
        results="النتائج", related_projects="مشاريع ذات صلة", related_news="أخبار ذات صلة",
        key_figures="أرقام رئيسية", governorates="المحافظات", target_group="الفئة المستهدفة",
        years_label="سنوات",
        today="اليوم",
        participants="المستفيدون", partner_label="الشريك", status="الحالة",
        years="السنوات", ongoing="مستمر", completed="مكتمل", content_needed="محتوى مطلوب",
        content_needed_note="هذا القسم جزء من الهيكل المعتمد، ولم يتم تزويدنا بالمادة المصدرية بعد.",
        credits="الصور والمصادر", sources="المصادر",
        download="تحميل PDF", no_download="لم يتم تزويدنا بالملف بعد",
        year_switch="السنة", female="إناث", male="ذكور", pwd="من ذوي الإعاقة",
        footer_about="مؤسسة فلسطينية مستقلة غير ربحية للبحث والمناصرة وبناء القدرات في الصحة والتعليم والتنمية — منذ عام 1989.",
        developed_by="تطوير",
    ),
}

# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------
HOME = {
    "en": dict(
        hero_badge="Since 1989",
        hero_title='A healthy, educated and <em>empowered</em> Palestinian society.',
        hero_lead="The Health Development Information and Policy Institute is an independent, non-profit "
                  "Palestinian organisation. We work through research, health education, educational support, "
                  "capacity building and advocacy — with women, youth, students and underserved communities "
                  "across the West Bank, Jerusalem and Gaza.",
        who_eyebrow="Who we are", who_title="An independent Palestinian institute, founded in 1989",
        who_body="HDIP was established in 1989 by a group of researchers, health practitioners and development "
                 "experts, in response to the urgent need to improve health care in Palestine. It conducts "
                 "specialised research, provides consultations and develops public policy across development "
                 "sectors — and advocates for the rights of marginalised groups, including women, youth and "
                 "persons with disabilities.",
        # The opening sentence of who_body, verbatim. The home page shows only
        # this; the full statement is on the About page, which the link beside
        # it points to.
        who_short='HDIP was established in 1989 by a group of researchers, health practitioners and development experts, in response to the urgent need to improve health care in Palestine.',
        who_facts=[("1989", "Founded in Ramallah"),
                   ("Independent", "Non-profit, non-governmental"),
                   ("35+ years", "Of research and advocacy")],
        impact_eyebrow="Impact in numbers", impact_title="Four years of results",
        impact_lead="Figures as reported by HDIP for each year. Switch between years to compare.",
        areas_eyebrow="Our work", areas_title="Five programme areas",
        areas_lead="Permanent areas of work. Each one carries its own activities, figures and related projects.",
        projects_eyebrow="Projects", projects_title="Featured projects",
        projects_lead="Funded initiatives with their own objectives, components and results.",
        where_eyebrow="Where we work", where_title="Eight governorates",
        where_lead="In 2024 HDIP delivered activities across the West Bank, Jerusalem and the Gaza Strip — "
                   "including educational support to students in displacement settings in Gaza.",
        news_eyebrow="Latest", news_title="News & stories",
        reports_eyebrow="Reports", reports_title="Annual reporting",
        reports_lead="The 2024 annual report covers strategic directions, activities, key outputs and recommendations.",
        partner_eyebrow="Partner with us", partner_title="Work with HDIP",
        partner_lead="HDIP works with local and international partners on research, training, evaluation and "
                     "community programmes.",
    ),
    "ar": dict(
        hero_badge="منذ عام 1989",
        hero_title='مجتمع فلسطيني صحي ومتعلّم <em>وممكّن</em>.',
        hero_lead="البرنامج الإعلامي للتطوير الصحي مؤسسة فلسطينية مستقلة غير ربحية. نعمل من خلال البحث "
                  "والتثقيف الصحي والدعم التعليمي وبناء القدرات والمناصرة — مع النساء والشباب والطلبة "
                  "والمجتمعات المهمّشة في الضفة الغربية والقدس وقطاع غزة.",
        who_eyebrow="من نحن", who_title="مؤسسة فلسطينية مستقلة تأسست عام 1989",
        who_body="تأسس البرنامج الإعلامي للتطوير الصحي عام 1989 على يد مجموعة من الباحثين والممارسين الصحيين "
                 "وخبراء التنمية، استجابةً للحاجة الملحّة لتحسين واقع الرعاية الصحية في فلسطين. يجري البرنامج "
                 "البحوث المتخصصة ويقدّم الاستشارات ويطوّر السياسات العامة في مختلف القطاعات التنموية، كما يدافع "
                 "عن حقوق الفئات المهمّشة من النساء والشباب وذوي الإعاقة.",
        # The opening sentence of who_body, verbatim. The home page shows only
        # this; the full statement is on the About page, which the link beside
        # it points to.
        who_short='تأسس البرنامج الإعلامي للتطوير الصحي عام 1989 على يد مجموعة من الباحثين والممارسين الصحيين وخبراء التنمية، استجابةً للحاجة الملحّة لتحسين واقع الرعاية الصحية في فلسطين.',
        who_facts=[("1989", "تأسس في رام الله"),
                   ("مستقل", "غير ربحي وغير حكومي"),
                   ("أكثر من 35 عامًا", "من البحث والمناصرة")],
        impact_eyebrow="الأثر بالأرقام", impact_title="أربع سنوات من النتائج",
        impact_lead="الأرقام كما وردت في تقارير البرنامج لكل عام. بدّل بين الأعوام للمقارنة.",
        areas_eyebrow="مجالات عملنا", areas_title="خمسة مجالات برامجية",
        areas_lead="مجالات عمل دائمة، لكل منها أنشطتها وأرقامها ومشاريعها المرتبطة بها.",
        projects_eyebrow="المشاريع", projects_title="مشاريع مختارة",
        projects_lead="مبادرات ممولة لكل منها أهدافها ومكوّناتها ونتائجها.",
        where_eyebrow="أين نعمل", where_title="ثماني محافظات",
        where_lead="في عام 2024 نفّذ البرنامج أنشطته في الضفة الغربية والقدس وقطاع غزة — بما في ذلك دروس "
                   "تقوية للطلبة في خيم النزوح في غزة.",
        news_eyebrow="الأحدث", news_title="أخبار وقصص",
        reports_eyebrow="التقارير", reports_title="التقارير السنوية",
        reports_lead="يغطي تقرير عام 2024 التوجهات الاستراتيجية والأنشطة وأبرز المخرجات والتوصيات.",
        partner_eyebrow="كن شريكًا", partner_title="اعمل مع البرنامج",
        partner_lead="يعمل البرنامج مع شركاء محليين ودوليين في البحث والتدريب والتقييم والبرامج المجتمعية.",
    ),
}

# --------------------------------------------------------------------------
# About — from تعريف.docx
# --------------------------------------------------------------------------
ABOUT = {
    "en": dict(
        title="About HDIP",
        lead="Founded in 1989 by researchers, health practitioners and development experts, in response to "
             "the urgent need to improve health care in Palestine — particularly in the West Bank and the "
             "Gaza Strip — through a scientific and professional approach to research, planning and "
             "development policy.",
        who_title="Who we are",
        who=[
            "HDIP is an independent, non-profit Palestinian organisation. It dedicates its work to specialised "
            "research, consultancy and the development of public policy across development sectors.",
            "Over time its role expanded to advocating for the rights of marginalised groups in Palestinian "
            "society — women, youth and persons with disabilities — rooted in a conviction about the importance "
            "of social justice and equality of opportunity.",
            "The institute gives considerable attention to building a democratic Palestinian civil society "
            "founded on active participation, transparency and accountability. It provides accurate information, "
            "evaluation studies and specialised training programmes in health, systems management and "
            "development policy, in order to strengthen local institutions and improve the quality of services "
            "delivered to citizens.",
        ],
        vision_title="Our vision",
        vision="We seek to advance development in Palestine by enabling Palestinian society to reach its basic "
               "needs in health, education and social services, fairly and sustainably. We believe a strong and "
               "cohesive society begins with meeting these vital needs and with development policies that respond "
               "to citizens' aspirations and reflect their real priorities. We work in a spirit of responsibility "
               "and community partnership to support positive change and to establish the principles of social "
               "justice and good governance — towards a prosperous Palestinian future that guarantees dignity and "
               "opportunity for all.",
        mission_title="Our mission",
        mission="HDIP seeks to contribute actively to building a Palestinian society founded on social and "
                "economic justice, which upholds the values of freedom, democracy and human rights. The programme "
                "works by implementing activities and initiatives that strengthen Palestinian capacities, open "
                "horizons for constructive dialogue and meet urgent community needs. We believe purposeful media "
                "is a tool for change, a platform for the citizen's voice, and a bridge towards a more aware and "
                "solidary society. Through it we seek to establish a culture of community participation, to "
                "stimulate critical thinking, and to support policies that place people at the heart of development.",
        objectives_title="Our objectives",
        objectives_lead="The fifteen general objectives set out in HDIP's founding profile.",
        objectives=[
            "Conduct research and studies on health and development conditions and on health and development policies.",
            "Hold seminars, meetings and conferences, and issue publications, research, books, periodicals and booklets in its field.",
            "Run programmes and training courses, and provide research, training, media and technical services in health and development, administration, administrative development and development planning.",
            "Raise the level of health and development awareness, and establish health information and research databases.",
            "Conduct dialogues and coordination activities to improve cooperation between civil society organisations and the relevant ministries, in order to improve coordination and rationalise the use of development resources.",
            "Provide advice and organise the scientific and technical activities that assist in preparing and adopting appropriate health, social and development legislation.",
            "Prepare, publish and document research abstracts in a way that serves Palestinian researchers, academics and development policy makers.",
            "Provide the consultations, evaluations, studies and expertise needed to strengthen individuals and institutions.",
            "Publish information that contributes to developing health and development awareness and improving development capacities, and provide the advisory, research and technical services that support sound development planning.",
            "Cooperate with Arab and international institutions in health and development research and statistics, and in developing health and development policies.",
            "Organise health and development programmes and activities.",
            "Supply and assist students, researchers, planners and local councils with information.",
            "Issue maps, explanatory materials, publications, books and periodicals that follow health issues and general development policies.",
            "Develop cooperation and coordination in the health and development fields between civil society and governmental institutions, in a way that serves Palestinian society.",
            "Carry out media activities that support the cause of the Palestinian people and meet its needs.",
        ],
        approach_title="Our approach",
        partner_title="Why partner with us",
        team_title="Team & board",
    ),
    "ar": dict(
        title="عن البرنامج",
        lead="تأسس عام 1989 على يد مجموعة من الباحثين والممارسين الصحيين وخبراء التنمية، استجابةً للحاجة الملحّة "
             "لتحسين واقع الرعاية الصحية في فلسطين، لا سيما في الضفة الغربية وقطاع غزة، وذلك من خلال اعتماد "
             "منهج علمي ومهني في البحث والتخطيط وصياغة السياسات التنموية.",
        who_title="من نحن",
        who=[
            "يُعد البرنامج الإعلامي مؤسسة فلسطينية مستقلة غير ربحية، تكرّس جهودها لإجراء البحوث المتخصصة، "
            "وتقديم الاستشارات، وتطوير السياسات العامة في مختلف القطاعات التنموية.",
            "ومع مرور الوقت، توسّع دور البرنامج ليشمل الدفاع عن حقوق الفئات المهمّشة في المجتمع الفلسطيني، مثل "
            "النساء والشباب وذوي الإعاقة، انطلاقًا من إيمانه العميق بأهمية العدالة الاجتماعية والمساواة في الفرص.",
            "كما يولي المعهد اهتمامًا كبيرًا ببناء مجتمع مدني فلسطيني ديمقراطي، يقوم على أسس المشاركة الفاعلة "
            "والشفافية والمساءلة. ويقدّم مجموعة من الخدمات النوعية تشمل توفير المعلومات الدقيقة، وتنفيذ الدراسات "
            "التقييمية، وتنظيم برامج تدريبية متخصصة في مجالات الصحة وإدارة النظم وصياغة السياسات التنموية، بهدف "
            "تعزيز قدرات المؤسسات المحلية وتحسين جودة الخدمات المقدمة للمواطنين.",
        ],
        vision_title="رؤيتنا",
        vision="نسعى إلى تعزيز مسيرة التطوير والتنمية في فلسطين من خلال تمكين المجتمع الفلسطيني من الوصول العادل "
               "والمستدام إلى احتياجاته الأساسية في مجالات الصحة والتعليم والخدمات الاجتماعية. ونؤمن بأن بناء "
               "مجتمع قوي ومتماسك يبدأ من تلبية هذه الاحتياجات الحيوية، وصياغة سياسات تنموية تستجيب لتطلعات "
               "المواطنين وتعكس أولوياتهم الحقيقية. نعمل بروح المسؤولية والشراكة المجتمعية على دعم مبادرات التغيير "
               "الإيجابي، وترسيخ مبادئ العدالة الاجتماعية والحكم الرشيد، وصولًا إلى مستقبل فلسطيني مزدهر يضمن "
               "الكرامة والفرص للجميع.",
        mission_title="رسالتنا",
        mission="يسعى البرنامج الإعلامي للتطوير الصحي إلى الإسهام الفاعل في بناء مجتمع فلسطيني يقوم على أسس "
                "العدالة الاجتماعية والاقتصادية، ويُعلي من قيم الحرية والديمقراطية وحقوق الإنسان. ويعمل البرنامج "
                "من خلال تنفيذ أنشطة ومبادرات نوعية تُعزز من قدرات الإنسان الفلسطيني، وتفتح آفاق الحوار البنّاء، "
                "وتلبي الاحتياجات المجتمعية الملحّة. نؤمن بأن الإعلام الهادف هو أداة للتغيير، ومنبر لإيصال صوت "
                "المواطن، وجسر نحو مجتمع أكثر وعيًا وتضامنًا. ومن خلال هذا البرنامج، نسعى إلى ترسيخ ثقافة المشاركة "
                "المجتمعية، وتحفيز التفكير النقدي، ودعم السياسات التي تضع الإنسان في قلب عملية التنمية.",
        objectives_title="الأهداف العامة",
        objectives_lead="الأهداف العامة الخمسة عشر الواردة في الملف التعريفي للبرنامج.",
        objectives=[
            "إجراء الأبحاث والدراسات المتعلقة بالوضع الصحي والتنموي والسياسات الصحية والتنموية.",
            "عقد الندوات والاجتماعات والمؤتمرات وإصدار المنشورات والأبحاث والكتب والدوريات والكراسات في مجال اختصاصه.",
            "عقد البرامج والدورات التدريبية وتقديم الخدمات البحثية والتدريبية والإعلامية والتقنية في مجالات التطوير الصحي والتنموي والإدارة والتطوير الإداري والتخطيط التنموي.",
            "رفع مستوى الوعي الصحي والتنموي وإنشاء قواعد المعلومات والأبحاث الصحية.",
            "إجراء الحوارات وتنظيم أنشطة التنسيق لتحسين التعاون بين المؤسسات الأهلية والوزارات المختلفة، بهدف تحسين التنسيق وترشيد استخدام الموارد التنموية.",
            "تقديم المشورة وتنظيم النشاطات العلمية والتقنية التي تساعد في إعداد وإقرار التشريعات الصحية والاجتماعية والتنموية المناسبة.",
            "إعداد ونشر الملخصات البحثية وتوثيقها بما يخدم الباحثين والأكاديميين الفلسطينيين وصانعي السياسات التنموية.",
            "تقديم المشورات وأعمال التقييم والدراسات والخبرات اللازمة لتقوية الأفراد والمؤسسات.",
            "نشر المعلومات التي تساهم في تطوير الوعي الصحي والتنموي وتحسين القدرات التنموية، وتقديم الخدمات الاستشارية والبحثية والتقنية التي تساعد على التخطيط التنموي السليم.",
            "التعاون مع المؤسسات العربية والدولية في مجالات الأبحاث والإحصائيات الصحية والتنموية وتطوير السياسات الصحية والتنموية.",
            "تنظيم البرامج والنشاطات الصحية والتنموية.",
            "تزويد ومساعدة الطلبة والباحثين والمخططين والمجالس المحلية بالمعلومات.",
            "إصدار الخرائط والوسائل الإيضاحية والمنشورات والكتب والدوريات التي تتابع قضايا الصحة والسياسات التنموية العامة.",
            "تطوير التعاون والتنسيق في الحقول الصحية والتنموية بين المؤسسات الأهلية والحكومية بما يخدم المجتمع الفلسطيني.",
            "القيام بالنشاطات الإعلامية المختلفة بما يخدم دعم قضية الشعب الفلسطيني وتلبية احتياجاته.",
        ],
        approach_title="منهجيتنا",
        partner_title="لماذا الشراكة معنا",
        team_title="الفريق ومجلس الإدارة",
    ),
}

# --------------------------------------------------------------------------
# Programme areas — 5, per the approved structure
# --------------------------------------------------------------------------
AREAS = [
    dict(slug="health", icon="pulse", photo="women-able-session",
         en=dict(name="Health & Health Education",
                 purpose="Health awareness, first aid and preventive health for women, students and communities.",
                 overview="Health for All — awareness and health education. HDIP delivered a series of specialised "
                          "training courses in 2024 for different age and social groups: women, university students "
                          "and school students. The courses covered health, psychological and preventive topics, "
                          "building participants' capacities, improving their awareness of health issues and "
                          "behaviours, and strengthening the idea of health as a basic right.",
                 what_title="What we do",
                 what=[("First aid courses", "Theoretical and practical training on wounds, bleeding, fractures, burns, choking, fainting and CPR."),
                       ("Women's mental health", "Basic concepts of mental health, stress management, coping with anxiety and depression, and psychological support during pregnancy and childbirth."),
                       ("Health awareness", "Physical and psychological change, prevention of risky behaviours and building self-confidence."),
                       ("Disease prevention", "Chronic and infectious disease, maternal health, family planning and nutrition during pregnancy and breastfeeding."),
                       ("Environmental health", "Air and water pollution, the effects of chemicals, and improving environmental conditions for public health."),
                       ("Health education workshops", "School health, personal hygiene, first aid, healthy nutrition, environmental health, psychological first aid and child health.")],
                 figures=[("85", "first aid courses"), ("1,700", "students reached"),
                          ("210", "women in mental health courses"), ("420", "students in health education workshops")]),
         ar=dict(name="الصحة والتثقيف الصحي",
                 purpose="التوعية الصحية والإسعاف الأولي والصحة الوقائية للنساء والطلبة والمجتمعات.",
                 overview="برنامج الصحة للجميع: الوعي والتثقيف الصحي. نفّذ البرنامج الإعلامي للتطوير الصحي في عام "
                          "2024 سلسلة من الدورات التدريبية المتخصصة التي استهدفت فئات عمرية واجتماعية مختلفة "
                          "(نساء، طلاب جامعات، طلاب مدارس). غطّت هذه الدورات مجموعة واسعة من المواضيع الصحية "
                          "والنفسية والوقائية، مما ساهم في بناء قدرات المشاركين وتحسين وعيهم بالقضايا والسلوكيات "
                          "الصحية، وتعزيز مفهوم «الصحة للجميع» كحق أساسي.",
                 what_title="ماذا نقدّم",
                 what=[("دورات الإسعاف الأولي", "تدريب نظري وعملي على الجروح والنزيف والكسور والحروق والاختناق والإغماء وإنعاش القلب."),
                       ("الصحة النفسية للنساء", "أساسيات الصحة النفسية، إدارة الضغوط، التعامل مع القلق والاكتئاب، ودعم النساء نفسيًا خلال الحمل والولادة."),
                       ("التوعية الصحية", "التغيرات الجسدية والنفسية، الوقاية من السلوكيات الخطرة، وتعزيز الثقة بالنفس."),
                       ("الوقاية من الأمراض", "الأمراض المزمنة والمعدية، صحة الحامل، تنظيم الأسرة، والتغذية خلال الحمل والرضاعة."),
                       ("الصحة البيئية", "تلوث الهواء والماء، وتأثير المواد الكيميائية، وتحسين الظروف البيئية لتعزيز الصحة العامة."),
                       ("ورشات التثقيف الصحي", "الصحة المدرسية، النظافة الشخصية، الإسعافات الأولية، التغذية السليمة، الصحة البيئية، الإسعاف النفسي الطارئ، وصحة الطفل.")],
                 figures=[("85", "دورة إسعاف أولي"), ("1,700", "طالب وطالبة"),
                          ("210", "سيدة في دورات الصحة النفسية"), ("420", "طالبًا في ورشات التثقيف الصحي")])),

    dict(slug="education", icon="book", photo="youth-training",
         en=dict(name="Education",
                 purpose="Addressing learning loss and keeping students in education through crisis.",
                 overview="HDIP supports students facing learning gaps caused by school closures, interruptions to "
                          "education, teachers' strikes and conflict. Work covers supplementary teaching in core "
                          "subjects, life skills, awareness of the importance of education, and support for "
                          "students in displacement settings in Gaza.",
                 what_title="What we do",
                 what=[("Supplementary school courses", "English, mathematics, physics, Arabic, computer skills, science and life skills for grades 7 to 11."),
                       ("University courses", "Communication skills, Microsoft Office, Bisan accounting software, scientific research and management."),
                       ("Awareness workshops", "Cyberbullying and online exploitation, effective communication, research skills, choosing a specialisation, dropout risks, and the value of reading."),
                       ("Career guidance", "Workshops and dialogue sessions with professionals so students can explore academic and career pathways."),
                       ("Study support groups", "Peer groups for cooperation and knowledge sharing, plus a scientific research club in each library."),
                       ("Emergency delivery", "Educational support for students in displacement settings in Gaza, maintaining learning through severe disruption.")],
                 figures=[("345", "activities in 2024"), ("8,321", "participants"),
                          ("61%", "female participants"), ("355", "participants with disabilities")]),
         ar=dict(name="التعليم",
                 purpose="معالجة الفاقد التعليمي والحفاظ على استمرار الطلبة في التعليم رغم الأزمات.",
                 overview="يدعم البرنامج الطلبة الذين يواجهون فجوات تعليمية ناتجة عن إغلاق المدارس والانقطاعات في "
                          "التعليم وإضراب المعلمين والحرب. يشمل العمل دروس التقوية في المواد الأساسية والمهارات "
                          "الحياتية والتوعية بأهمية التعليم، ودعم الطلبة في خيم النزوح في غزة.",
                 what_title="ماذا نقدّم",
                 what=[("دورات مدرسية تعويضية", "اللغة الإنجليزية والرياضيات والفيزياء واللغة العربية والحاسوب والعلوم والمهارات الحياتية، من الصف السابع حتى الحادي عشر."),
                       ("دورات جامعية", "مهارات الاتصال، برامج الأوفيس، برنامج بيسان لطلبة المحاسبة، البحث العلمي، والإدارة."),
                       ("ورش التوعية", "الابتزاز الإلكتروني، الاتصال الفعّال، إعداد البحث العلمي، اختيار التخصصات، مخاطر التسرب المدرسي، وتشجيع القراءة."),
                       ("التوجيه المهني", "ورش عمل وجلسات حوارية مع مهنيين تساعد الطلبة على استكشاف مساراتهم الأكاديمية والمهنية."),
                       ("مجموعات الدعم الدراسي", "مجموعات طلابية للتعاون وتبادل المعرفة، إضافة إلى نادي للبحث العلمي في كل مكتبة."),
                       ("الاستجابة الطارئة", "دروس تقوية للطلبة في خيم النزوح في غزة للحفاظ على استمرار العملية التعليمية.")],
                 figures=[("345", "نشاطًا في 2024"), ("8,321", "مستفيدًا"),
                          ("61%", "نسبة الإناث"), ("355", "من ذوي الإعاقة")])),

    dict(slug="women", icon="users", photo="women-leaders-training",
         en=dict(name="Women's Empowerment",
                 purpose="Women's leadership, political participation and rights in local communities.",
                 overview="HDIP works with women as leaders, candidates and community representatives — not only "
                          "as voters. Training covers feminist leadership, political participation, gender equality, "
                          "human rights, the family protection law, non-violence, first aid and mental health, "
                          "alongside coalition building and advocacy.",
                 what_title="What we do",
                 what=[("Leadership training", "Feminist leadership, political participation, the electoral process and campaign management."),
                       ("Rights and legal awareness", "Gender equality, human rights, the family protection law and non-violence."),
                       ("Coalition building", "Meetings that identify shared goals and issues across women's groups and communities."),
                       ("Experience sharing", "Direct meetings with women who have previously stood in elections."),
                       ("Health and wellbeing", "First aid and mental health training delivered within the women's programme."),
                       ("Public platforms", "Conferences that bring women and decision-makers into the same room.")],
                 figures=[("200+", "women and men at the closing conference"), ("4", "governorates"),
                          ("16", "sites per governorate"), ("10", "coalition-building meetings")]),
         ar=dict(name="تمكين المرأة",
                 purpose="قيادة النساء ومشاركتهن السياسية وحقوقهن في المجتمعات المحلية.",
                 overview="يعمل البرنامج مع النساء كقياديات ومرشحات وممثلات لمجتمعاتهن، لا كناخبات فقط. تشمل "
                          "التدريبات القيادة النسوية والمشاركة السياسية والمساواة الجندرية وحقوق الإنسان وقانون "
                          "حماية الأسرة واللاعنف والإسعافات الأولية والصحة النفسية، إلى جانب بناء التحالفات "
                          "والمناصرة.",
                 what_title="ماذا نقدّم",
                 what=[("التدريب القيادي", "القيادة النسوية، المشاركة السياسية، العملية الانتخابية، وإدارة الحملات الانتخابية."),
                       ("الوعي بالحقوق والقانون", "المساواة الجندرية، حقوق الإنسان، قانون حماية الأسرة، واللاعنف."),
                       ("بناء التحالفات", "لقاءات لتحديد الأهداف والقضايا المشتركة بين المجموعات النسوية والمجتمعات."),
                       ("تبادل الخبرات", "لقاءات مباشرة مع نساء سبق أن خضن التجربة الانتخابية."),
                       ("الصحة والعافية", "تدريبات في الإسعافات الأولية والصحة النفسية ضمن البرنامج النسوي."),
                       ("المنصات العامة", "مؤتمرات تجمع النساء وصانعي القرار في مكان واحد.")],
                 figures=[("200+", "امرأة ورجلًا في المؤتمر الختامي"), ("4", "محافظات"),
                          ("16", "موقعًا في كل محافظة"), ("10", "لقاءات لبناء التحالفات")])),

    dict(slug="youth", icon="vote", photo="youth-training",
         en=dict(name="Youth & Civic Leadership",
                 purpose="University students as informed, responsible and community-oriented leaders.",
                 overview="HDIP invests in young people's potential by providing knowledge, leadership skills and "
                          "practical tools to engage constructively in their universities and communities — "
                          "combining leadership development with human rights education, critical thinking, "
                          "teamwork and advocacy.",
                 what_title="What we do",
                 what=[("Leadership training", "Participatory and democratic leadership, respect for diversity and different opinions, teamwork and collaborative decision-making."),
                       ("Human rights education", "Fundamental human and civic rights, mechanisms for promoting and defending them, and rights issues in local and international contexts."),
                       ("Advocacy skills", "Identifying community issues and priorities, planning advocacy campaigns, and developing messages for community engagement."),
                       ("Youth networks", "Exchange of experience and ideas among students from different universities, and cooperation between academic institutions and local communities.")],
                 figures=[("3", "day intensive training"), ("Multiple", "universities represented"),
                          ("Leadership", "rights and advocacy combined"), ("2024", "programme year")]),
         ar=dict(name="الشباب والقيادة المدنية",
                 purpose="طلبة الجامعات كقادة واعين ومسؤولين ومنخرطين في مجتمعاتهم.",
                 overview="يستثمر البرنامج في طاقات الشباب عبر تزويدهم بالمعرفة والمهارات القيادية والأدوات العملية "
                          "التي تؤهلهم للانخراط البنّاء في محيطهم الجامعي والمجتمعي، بالجمع بين تطوير القيادة "
                          "والتثقيف بحقوق الإنسان والتفكير النقدي والعمل الجماعي والمناصرة.",
                 what_title="ماذا نقدّم",
                 what=[("التدريب القيادي", "القيادة التشاركية والديمقراطية، احترام التنوع والرأي الآخر، العمل الجماعي واتخاذ القرار التشاركي."),
                       ("التثقيف بحقوق الإنسان", "الحقوق الأساسية والمدنية، وآليات تعزيزها والدفاع عنها، وقضايا الحقوق محليًا ودوليًا."),
                       ("مهارات المناصرة", "تحديد القضايا والأولويات المجتمعية، التخطيط لحملات المناصرة، وصياغة الرسائل للانخراط المجتمعي."),
                       ("الشبكات الشبابية", "تبادل الخبرات والأفكار بين طلبة الجامعات المختلفة، والتعاون بين المؤسسات الأكاديمية والمجتمعات المحلية.")],
                 figures=[("3", "أيام تدريب مكثف"), ("عدة", "جامعات مشاركة"),
                          ("القيادة", "والحقوق والمناصرة معًا"), ("2024", "سنة البرنامج")])),

    dict(slug="research", icon="search", photo="women-able-group",
         en=dict(name="Research, Policy & Knowledge",
                 purpose="Scientific research, evidence and knowledge-sharing as the basis of policy.",
                 overview="HDIP conducts research and studies on health and development conditions and policies, "
                          "and works to raise awareness of the value of scientific research among students, "
                          "researchers and academic communities. In 2024 this took the form of targeted campaigns, "
                          "workshops, lectures and seminars, alongside the dissemination of educational material.",
                 what_title="What we do",
                 what=[("Research campaigns", "Workshops, lectures and seminars encouraging students, researchers and academic communities to engage in research."),
                       ("Knowledge dissemination", "Publishing information and educational materials related to health and development."),
                       ("Research clubs", "A scientific research club established in each library to encourage inquiry and critical thinking."),
                       ("Capacity building", "Specialised training in health education, health systems and preventive approaches for community members, particularly women and youth."),
                       ("Policy dialogue", "Coordination activities to improve cooperation between civil society organisations and ministries.")],
                 figures=[("Workshops", "lectures and seminars"), ("1 per library", "scientific research club"),
                          ("Evidence", "based approaches"), ("2024", "reporting year")]),
         ar=dict(name="البحث والسياسات والمعرفة",
                 purpose="البحث العلمي والأدلة وتبادل المعرفة كأساس للسياسات.",
                 overview="يجري البرنامج الأبحاث والدراسات المتعلقة بالوضع الصحي والتنموي والسياسات، ويعمل على رفع "
                          "الوعي بأهمية البحث العلمي لدى الطلبة والباحثين والمجتمع الأكاديمي. وفي عام 2024 اتخذ ذلك "
                          "شكل حملات موجهة وورش عمل ومحاضرات وندوات، إلى جانب نشر المواد التعليمية.",
                 what_title="ماذا نقدّم",
                 what=[("حملات البحث العلمي", "ورش عمل ومحاضرات وندوات تشجّع الطلبة والباحثين والمجتمع الأكاديمي على الانخراط في البحث."),
                       ("نشر المعرفة", "نشر المعلومات والمواد التعليمية المتعلقة بالصحة والتنمية."),
                       ("أندية البحث", "تشكيل نادٍ للبحث العلمي في كل مكتبة لتشجيع الاستقصاء والتفكير النقدي."),
                       ("بناء القدرات", "تدريب متخصص في التثقيف الصحي وإدارة النظم الصحية والسياسات الوقائية لأفراد المجتمع، خاصة النساء والشباب."),
                       ("حوار السياسات", "أنشطة تنسيق لتحسين التعاون بين المؤسسات الأهلية والوزارات.")],
                 figures=[("ورش", "ومحاضرات وندوات"), ("نادٍ لكل مكتبة", "للبحث العلمي"),
                          ("مقاربات", "قائمة على الأدلة"), ("2024", "سنة التقرير")])),
]

# --------------------------------------------------------------------------
# Projects — 4, per the approved structure
# --------------------------------------------------------------------------
PROJECTS = [
    dict(slug="right-to-education", area="education", photo="youth-training",
         status="ongoing", years="2024", partner=None,
         en=dict(name="Right to Education",
                 tagline="Keeping students learning through closure, displacement and war.",
                 glance=[("Governorates", "8, including Gaza"), ("Target group", "School and university students"),
                         ("Participants", "8,321 in 2024"), ("Activities", "345 in 2024")],
                 about="The Right to Education Project aims to support a generation of Palestinian students who are "
                       "better equipped to develop themselves and contribute to their communities, particularly in "
                       "marginalised and underserved areas. Despite significant challenges — school closures, "
                       "violence, displacement, interruptions to education and the war in Gaza — HDIP continued "
                       "implementing the project in 2024 through an emergency-adapted approach across eight "
                       "governorates, including Gaza.",
                 objectives=[
                     "Raise students' awareness of the importance of education as a means of individual and community development.",
                     "Strengthen students' scientific, analytical, creative and problem-solving skills, improving their future educational and employment opportunities.",
                     "Provide educational and skills-based training for school students, particularly those from disadvantaged and marginalised backgrounds.",
                     "Support students to improve academic performance, particularly in science, mathematics and languages.",
                     "Address learning gaps resulting from COVID-19 disruptions, interruptions to education and teachers' strikes.",
                     "Contribute to reducing school dropout and support students in identifying appropriate educational and university pathways.",
                     "Develop students' life skills, communication skills and ability to overcome challenges.",
                 ],
                 components=[
                     ("Trainer evaluation and capacity building",
                      "Evaluation meetings with trainers across project locations — face to face in Ramallah and Abu Dis, online with Nablus, Tulkarm, Jenin, Bethlehem and Hebron. Meetings were documented through formal minutes, and produced corrective action plans and monthly work plans for each centre."),
                     ("Awareness workshops on the importance of education",
                      "112 workshops in Hebron, Bethlehem, Abu Dis, Ramallah, Tulkarm, Jenin and Nablus, covering cyberbullying and online exploitation, effective communication, scientific research skills, choice of specialisation, dropout risks, and the importance of education and reading."),
                     ("School educational and training courses",
                      "170 courses through centres in the West Bank and Gaza — English, mathematics, physics, Arabic, computer skills, science and life skills. Each course ran roughly 10 to 20 sessions, targeting grades 7 to 11, with particular attention to subjects where students experienced difficulty."),
                     ("University educational and training courses",
                      "63 courses for university students in the West Bank, covering communication skills, Microsoft Office, Bisan accounting software for accounting students, scientific research and management skills."),
                 ],
                 table_head=["Activity", "Activities", "Participants", "Male", "Female", "With disabilities"],
                 table=[["Right to Education workshops", "112", "2,842", "1,319", "1,523", "121"],
                        ["School courses", "170", "4,403", "1,565", "2,838", "210"],
                        ["University courses", "63", "1,076", "348", "728", "24"],
                        ["Total", "345", "8,321", "3,232", "5,089", "355"]],
                 results=[
                     "345 activities implemented across the targeted areas.",
                     "8,321 participants reached, 61% of them female.",
                     "355 persons with disabilities participated in project activities.",
                     "Educational support extended to students affected by conflict, displacement and interruption to formal education, including in displacement settings in Gaza.",
                 ]),
         ar=dict(name="الحق في التعليم",
                 tagline="استمرار تعليم الطلبة رغم الإغلاق والنزوح والحرب.",
                 glance=[("المحافظات", "8 بما فيها غزة"), ("الفئة المستهدفة", "طلبة المدارس والجامعات"),
                         ("المستفيدون", "8,321 في 2024"), ("الأنشطة", "345 في 2024")],
                 about="يهدف مشروع الحق في التعليم إلى تكوين جيل من الطلاب الفلسطينيين قادرين على تطوير أنفسهم "
                       "ومجتمعاتهم، خاصة في المناطق المهمّشة. ورغم الظروف الصعبة — إغلاق المدارس والعنف والنزوح "
                       "والانقطاعات في التعليم والحرب على قطاع غزة واجتياح مخيمي جنين وطولكرم — تمكّن البرنامج من "
                       "تنفيذ المشروع في عام 2024 ضمن خطة طوارئ شاملة في ثماني محافظات بما فيها قطاع غزة.",
                 objectives=[
                     "زيادة الوعي لدى الطلاب حول أهمية التعليم كوسيلة لتنمية الفرد والمجتمع.",
                     "تحسين القدرة العلمية والتحليلية والإبداعية للطلاب وبالتالي تحسين فرصهم التعليمية والمهنية.",
                     "تدريب طلبة المدارس ذكورًا وإناثًا، وخاصة من الفئات المهمّشة والفقيرة.",
                     "مساعدتهم على تحسين مستوى تعليمهم المدرسي خاصة في العلوم والرياضيات واللغات.",
                     "تعويضهم عن النقص الناجم عن فترة كورونا والانقطاعات في التعليم وفترة إضراب المعلمين.",
                     "المساهمة في الحد من التسرب المدرسي وتحديد توجهاتهم العلمية والجامعية.",
                     "تنمية المهارات الحياتية ومهارات التواصل والقدرة على تجاوز العقبات.",
                 ],
                 components=[
                     ("لقاءات تقييمية للمدربين وبناء القدرات",
                      "عُقدت لقاءات تقييمية للمدربين في مختلف المناطق، وجاهية في مركزي رام الله وأبو ديس، وعبر الإنترنت مع مراكز نابلس وطولكرم وجنين وبيت لحم والخليل. وُثّقت اللقاءات بمحاضر رسمية، وخرجت بخطة علاجية وخطة عمل شهرية لكل مركز."),
                     ("ورش توعية حول أهمية التعليم",
                      "112 ورشة في الخليل وبيت لحم وأبو ديس ورام الله وطولكرم وجنين ونابلس، تناولت الابتزاز الإلكتروني والاتصال الفعّال وإعداد البحث العلمي واختيار التخصصات ومخاطر التسرب المدرسي وأهمية التعليم وتشجيع القراءة."),
                     ("الدورات التعليمية والتدريبية المدرسية",
                      "170 دورة عبر مراكز الضفة الغربية وغزة، شملت اللغة الإنجليزية والرياضيات والفيزياء واللغة العربية والحاسوب والعلوم والمهارات الحياتية. تراوحت كل دورة بين عشرة وعشرين لقاءً واستهدفت الصفوف من السابع حتى الحادي عشر."),
                     ("الدورات التعليمية والتدريبية الجامعية",
                      "63 دورة لطلبة الجامعات في الضفة الغربية، شملت مهارات الاتصال وبرامج الأوفيس وبرنامج بيسان لطلبة المحاسبة والبحث العلمي ومهارات الإدارة."),
                 ],
                 table_head=["النشاط", "عدد الأنشطة", "المستفيدون", "ذكور", "إناث", "ذوو إعاقة"],
                 table=[["ورش الحق في التعليم", "112", "2,842", "1,319", "1,523", "121"],
                        ["دورات المدارس", "170", "4,403", "1,565", "2,838", "210"],
                        ["دورات الجامعات", "63", "1,076", "348", "728", "24"],
                        ["المجموع الكلي", "345", "8,321", "3,232", "5,089", "355"]],
                 results=[
                     "تنفيذ 345 نشاطًا في المناطق المستهدفة.",
                     "الوصول إلى 8,321 مستفيدًا ومستفيدة، 61% منهم إناث.",
                     "مشاركة 355 شخصًا من ذوي الإعاقة في أنشطة المشروع.",
                     "تقديم الدعم التعليمي للطلبة المتأثرين بالحرب والنزوح وانقطاع التعليم، بما في ذلك في خيم النزوح في غزة.",
                 ])),

    dict(slug="women-able", area="women", photo="conference-closing",
         status="completed", years="2020–2024", partner="Olof Palme International Center",
         en=dict(name="Women Able to Change Society",
                 tagline="Five years of women's leadership across four governorates.",
                 glance=[("Governorates", "Hebron, Jenin, Tulkarm, Ramallah"), ("Target group", "Women and youth aged 18–30"),
                         ("Trainees", "35 per governorate"), ("Sites", "16 per governorate")],
                 about="Over five years the project was implemented in four main West Bank governorates. It targeted "
                       "women and youth aged 18 to 30 — university students, graduates and homemakers. In each "
                       "governorate 35 trainees took part, working with 16 sites (a village or town each), with one "
                       "trainee selected from every site to act as a link to the women's groups in her area.",
                 objectives=[
                     "Raise awareness of women's rights and the importance of their participation in local elections.",
                     "Deliver comprehensive training in feminist leadership, political participation, gender equality and human rights.",
                     "Build knowledge of the family protection law and the principles of non-violence.",
                     "Equip women to express themselves and defend their rights, increasing their opportunity to stand in local elections.",
                     "Create spaces where women can bring their issues directly to decision-makers.",
                 ],
                 components=[
                     ("Training in 2024",
                      "The project continued delivering training through 2024, with trainees receiving further sessions in feminist leadership, gender and non-violence."),
                     ("Coalition building",
                      "10 coalition-building meetings for 30 participants, identifying shared goals and issues including discussion of the family protection law. A training seminar was also held in Ramallah for 52 participants, allowing exchange of experience and strengthening of skills."),
                     ("Closing conference",
                      "A closing conference was held in Ramallah where more than 200 women and men met decision-makers. The conference gave women a platform to raise their issues and experiences, contributing significantly to their empowerment and to strengthening their participation in political and social life."),
                     ("Success stories",
                      "At the closing conference women told their own success stories — demonstrating their ability to share their experience and to invite other women to take part, reflecting the behavioural change and positive impact of the training and empowerment programmes."),
                 ],
                 results=[
                     "A marked change in women's behaviour and self-confidence between the start and the end of the project.",
                     "At the outset many women had low self-confidence, which limited their participation in social and political activity.",
                     "There was a significant gap in awareness of their legal and social rights, leaving them hesitant to claim those rights.",
                     "As the project progressed, women became markedly more confident, more ready to express their opinions and to take part in events.",
                     "Awareness of legal and social rights rose, helping them claim those rights more effectively.",
                 ]),
         ar=dict(name="نساء قادرات على تغيير المجتمع",
                 tagline="خمس سنوات من القيادة النسوية في أربع محافظات.",
                 glance=[("المحافظات", "الخليل، جنين، طولكرم، رام الله"), ("الفئة المستهدفة", "النساء والشباب 18–30 عامًا"),
                         ("المتدربات", "35 في كل محافظة"), ("المواقع", "16 في كل محافظة")],
                 about="على مدار خمسة أعوام، نُفّذ المشروع في أربع محافظات رئيسية في الضفة الغربية. استهدف النساء "
                       "والشباب من الفئة العمرية بين 18 و30 عامًا، بما في ذلك طالبات الجامعات والخريجات وربات "
                       "البيوت. في كل محافظة شاركت 35 متدربة، وتم العمل مع 16 موقعًا (قرية أو بلدة) في كل محافظة، "
                       "حيث اختيرت متدربة واحدة من كل موقع لتكون حلقة وصل مع المجموعات النسائية في منطقتها.",
                 objectives=[
                     "رفع الوعي بحقوق المرأة وأهمية مشاركتها في الانتخابات المحلية.",
                     "تقديم تدريبات شاملة في القيادة النسوية والمشاركة السياسية والمساواة الجندرية وحقوق الإنسان.",
                     "بناء المعرفة بقانون حماية الأسرة ومبادئ اللاعنف.",
                     "تمكين النساء من التعبير عن أنفسهن والدفاع عن حقوقهن، بما يزيد فرصهن في الترشح للانتخابات المحلية.",
                     "خلق مساحات تلتقي فيها النساء بصانعي القرار مباشرة.",
                 ],
                 components=[
                     ("استكمال المشروع في 2024",
                      "استمر المشروع في تقديم التدريبات خلال عام 2024، حيث تلقت المتدربات مزيدًا من التدريب في القيادة النسوية والجندر واللاعنف."),
                     ("بناء التحالفات",
                      "تم تنظيم 10 لقاءات لبناء التحالفات استهدفت 30 مشاركًا ومشاركة، حُدّدت خلالها الأهداف والقضايا المشتركة، بما في ذلك نقاشات حول قانون حماية الأسرة. كما عُقدت ندوة تدريبية في رام الله لـ 52 مشاركًا ومشاركة."),
                     ("المؤتمر الختامي",
                      "في ختام الأنشطة نُظّم مؤتمر ختامي في رام الله، التقى فيه أكثر من 200 امرأة ورجل بصانعي القرار. أتاح المؤتمر للنساء منصة لطرح قضاياهن وتجاربهن، مما أسهم في تمكينهن وتعزيز مشاركتهن في الحياة السياسية والاجتماعية."),
                     ("قصص النجاح",
                      "خلال المؤتمر الختامي روت النساء قصص نجاحهن، وأظهرن قدرتهن على مشاركة تجاربهن ودعوة نساء أخريات لخوض التجربة، بما يعكس التغير السلوكي والأثر الإيجابي لبرامج التدريب والتمكين."),
                 ],
                 results=[
                     "تحوّل ملحوظ في سلوك النساء وثقتهن بأنفسهن بين بداية المشروع ونهايته.",
                     "في البداية كانت العديد من النساء تعاني من انخفاض الثقة بالنفس، مما أثّر سلبًا على مشاركتهن في الأنشطة الاجتماعية والسياسية.",
                     "كانت هناك فجوة كبيرة في الوعي بحقوقهن القانونية والاجتماعية، مما أدى إلى ترددهن في المطالبة بها.",
                     "مع تقدّم المشروع شهدت النساء تحسنًا كبيرًا في ثقتهن بأنفسهن، وأصبحن أكثر استعدادًا للتعبير عن آرائهن والمشاركة في الفعاليات.",
                     "ارتفعت مستويات الوعي بالحقوق القانونية والاجتماعية، مما ساعدهن على المطالبة بحقوقهن بشكل أكثر فعالية.",
                 ])),

    dict(slug="women-leaders", area="women", photo="women-leaders-training",
         status="ongoing", years="2024", partner=None,
         en=dict(name="Women Leaders in Local Councils",
                 tagline="Towards effective women's political participation in local communities.",
                 glance=[("Format", "3-day intensive"), ("Training hours", "30"),
                         ("Focus", "Candidacy and local councils"), ("Target group", "Women in local communities")],
                 about="The project was designed to strengthen women's participation in local public life and "
                       "increase their knowledge and capacity to engage in decision-making. It focused on supporting "
                       "women not only as voters, but as potential candidates and community representatives, with an "
                       "emphasis on leadership skills, electoral processes, communication, advocacy and community "
                       "engagement.",
                 objectives=[
                     "Strengthen women's knowledge and confidence regarding participation in electoral processes.",
                     "Encourage women to consider candidacy for leadership positions in local councils.",
                     "Support the development of women's groups and networks that can advocate for women's rights and community concerns.",
                     "Increase awareness of legal and policy issues related to women's protection, including domestic violence.",
                     "Address negative social perceptions and stereotypes affecting women's participation in public life.",
                     "Promote awareness of civic and political participation among women, particularly in underserved communities.",
                 ],
                 components=[
                     ("Intensive leadership and political participation training",
                      "An intensive three-day programme comprising 30 training hours, bringing together women from different communities. The training covered women's leadership and political participation, the electoral process, experience sharing among participants, election campaign management, communication and negotiation skills, and community coalition and alliance building."),
                     ("Experience-sharing sessions with women leaders",
                      "Direct meetings with women who had previously participated in elections. The sessions gave participants the chance to hear first-hand experience, discuss the challenges encountered, exchange practical lessons and strategies, and ask questions about public and political participation."),
                 ],
                 results=[
                     "Increased political and civic awareness — greater understanding of electoral processes and the role women can play in local decision-making.",
                     "Strengthened leadership skills — practical skills in communication, negotiation, campaign planning, teamwork and coalition building.",
                     "Increased readiness to consider candidacy, through learning the practical requirements and challenges of electoral participation.",
                     "Increased confidence and peer learning through interaction with other participants and with women who had stood before.",
                     "Greater awareness of the barriers to women's participation — social perceptions, stereotypes and practical challenges.",
                 ]),
         ar=dict(name="نساء قياديات في المجالس المحلية",
                 tagline="نحو مشاركة سياسية فاعلة للنساء في المجتمعات المحلية.",
                 glance=[("الشكل", "تدريب مكثف 3 أيام"), ("ساعات التدريب", "30"),
                         ("التركيز", "الترشح والمجالس المحلية"), ("الفئة المستهدفة", "النساء في المجتمعات المحلية")],
                 about="صُمّم المشروع لتعزيز مشاركة النساء في الحياة العامة المحلية وزيادة معرفتهن وقدرتهن على "
                       "الانخراط في عمليات صنع القرار. وركّز على دعم النساء لا كناخبات فحسب، بل كمرشحات محتملات "
                       "وممثلات لمجتمعاتهن، مع التركيز على المهارات القيادية والعمليات الانتخابية والاتصال "
                       "والمناصرة والانخراط المجتمعي.",
                 objectives=[
                     "تعزيز معرفة النساء وثقتهن فيما يتعلق بالمشاركة في العمليات الانتخابية.",
                     "تشجيع النساء على التفكير في الترشح لمواقع قيادية في المجالس المحلية.",
                     "دعم تطوير المجموعات والشبكات النسوية القادرة على المناصرة لحقوق المرأة وقضايا المجتمع.",
                     "زيادة الوعي بالقضايا القانونية والسياساتية المتعلقة بحماية المرأة، بما في ذلك العنف الأسري.",
                     "معالجة التصورات الاجتماعية السلبية والصور النمطية التي تؤثر على مشاركة النساء في الحياة العامة.",
                     "تعزيز الوعي بالمشاركة المدنية والسياسية لدى النساء، خاصة في المجتمعات المهمّشة.",
                 ],
                 components=[
                     ("تدريب مكثف في القيادة والمشاركة السياسية",
                      "برنامج تدريبي مكثف على مدار ثلاثة أيام شمل 30 ساعة تدريبية، جمع نساءً من مجتمعات مختلفة. غطّى التدريب القيادة النسوية والمشاركة السياسية، والعملية الانتخابية، وتبادل الخبرات بين المشاركات، وإدارة الحملات الانتخابية، ومهارات الاتصال والتفاوض، وبناء التحالفات المجتمعية."),
                     ("جلسات تبادل الخبرات مع نساء قياديات",
                      "لقاءات مباشرة مع نساء سبق أن شاركن في الانتخابات. أتاحت الجلسات للمشاركات الاستماع إلى تجارب مباشرة، ومناقشة التحديات التي واجهتهن، وتبادل الدروس والاستراتيجيات العملية، وطرح الأسئلة حول المشاركة العامة والسياسية."),
                 ],
                 results=[
                     "زيادة الوعي السياسي والمدني — فهم أعمق للعمليات الانتخابية ولدور النساء في صنع القرار المحلي.",
                     "تعزيز المهارات القيادية — مهارات عملية في الاتصال والتفاوض وتخطيط الحملات والعمل الجماعي وبناء التحالفات.",
                     "زيادة الاستعداد للتفكير في الترشح، عبر التعرف على المتطلبات والتحديات العملية للمشاركة الانتخابية.",
                     "زيادة الثقة والتعلّم من الأقران عبر التفاعل مع المشاركات ومع نساء سبق أن خضن التجربة.",
                     "وعي أكبر بالعوائق أمام مشاركة النساء — التصورات الاجتماعية والصور النمطية والتحديات العملية.",
                 ])),

    dict(slug="youth-leadership", area="youth", photo="youth-training",
         status="ongoing", years="2024", partner="Friedrich-Ebert-Stiftung",
         en=dict(name="Young Leadership in Universities",
                 tagline="University students as active, responsible and community-oriented leaders.",
                 glance=[("Format", "3-day intensive"), ("Target group", "University students"),
                         ("Focus", "Leadership, rights, advocacy"), ("Partner", "Friedrich-Ebert-Stiftung")],
                 about="The project aims to empower university students to play an active role in building a more "
                       "informed and progressive society. It invests in young people's potential by providing them "
                       "with knowledge, leadership skills and practical tools to engage constructively in their "
                       "universities and communities.",
                 objectives=[
                     "Increase knowledge and awareness of leadership, community participation and civil rights among university students.",
                     "Develop leadership skills through practical workshops and training focused on teamwork, decision-making and effective communication.",
                     "Promote community engagement by encouraging students to participate in volunteer activities and local initiatives.",
                     "Build a youth leadership network that facilitates exchange of experience and ideas among students from different universities, and encourages cooperation between academic institutions and local communities.",
                 ],
                 components=[
                     ("Leadership training",
                      "Principles of participatory and democratic leadership, respect for diversity and different opinions, and teamwork and collaborative decision-making."),
                     ("Human rights education",
                      "Fundamental human rights and civic rights, mechanisms for promoting and defending rights, and human rights issues in local and international contexts."),
                     ("Advocacy and campaigning",
                      "Identifying community issues and priorities, planning advocacy campaigns, developing messages and approaches for community engagement, and using advocacy tools to influence relevant policies and practices."),
                 ],
                 results=[
                     "Increased self-confidence — practising leadership and communication skills gave students greater confidence in expressing their ideas and taking part in group activities.",
                     "Strengthened social and professional relationships through interaction with peers and academic stakeholders.",
                     "Improved leadership and practical skills — teamwork, communication, decision-making, leadership and advocacy, transferable to future study and employment.",
                     "Enhanced critical thinking — interactive discussion encouraged students to analyse issues, weigh perspectives and make informed decisions.",
                     "Increased community engagement — students came to see themselves as active participants in their communities.",
                     "Stronger youth leadership potential, combining leadership training, human rights education and advocacy skills.",
                 ]),
         ar=dict(name="تعزيز القيادات الشابة في الجامعات",
                 tagline="طلبة الجامعات كقادة فاعلين ومسؤولين ومنخرطين في مجتمعاتهم.",
                 glance=[("الشكل", "تدريب مكثف 3 أيام"), ("الفئة المستهدفة", "طلبة الجامعات"),
                         ("التركيز", "القيادة والحقوق والمناصرة"), ("الشريك", "مؤسسة فريدريش إيبرت")],
                 about="يهدف المشروع إلى تمكين الشباب الجامعي من لعب دور فاعل في بناء مجتمع أكثر وعيًا وتقدمًا على "
                       "المستويات السياسية والاجتماعية والاقتصادية. ينطلق المشروع من إيمان عميق بأهمية الاستثمار في "
                       "طاقات الشباب، وتزويدهم بالمعرفة والمهارات التي تؤهلهم ليكونوا قادة مؤثرين في محيطهم الجامعي "
                       "والمجتمعي.",
                 objectives=[
                     "تعزيز الوعي والمعرفة لدى الطلبة حول مفاهيم القيادة والمشاركة المجتمعية والحقوق المدنية.",
                     "تطوير المهارات القيادية من خلال ورش عمل ودورات تدريبية تركز على إدارة الفريق واتخاذ القرار والتواصل الفعّال.",
                     "تشجيع الانخراط المجتمعي عبر تحفيز الطلبة على المشاركة في الأنشطة التطوعية والمبادرات المحلية.",
                     "بناء شبكة قيادية شبابية تتيح تبادل الخبرات والأفكار بين الطلبة من مختلف الجامعات، وتفتح المجال للتعاون بين المؤسسات الأكاديمية والمجتمعات المحلية.",
                 ],
                 components=[
                     ("التدريب القيادي",
                      "مبادئ القيادة التشاركية والديمقراطية، واحترام التنوع والرأي الآخر، والعمل الجماعي واتخاذ القرار التشاركي."),
                     ("التثقيف بحقوق الإنسان",
                      "الحقوق الأساسية والمدنية، وآليات تعزيز الحقوق والدفاع عنها، وقضايا حقوق الإنسان في السياقين المحلي والدولي."),
                     ("المناصرة والحملات",
                      "تحديد القضايا والأولويات المجتمعية، والتخطيط لحملات المناصرة، وصياغة الرسائل وأساليب الانخراط المجتمعي، واستخدام أدوات المناصرة للتأثير في السياسات والممارسات."),
                 ],
                 results=[
                     "زيادة الثقة بالنفس — أتاحت المشاركة في الأنشطة القيادية للطلبة ممارسة مهارات القيادة والتواصل، مما عزّز ثقتهم في التعبير عن أفكارهم.",
                     "تعزيز العلاقات الاجتماعية والمهنية عبر التفاعل مع الأقران والجهات الأكاديمية.",
                     "تحسين المهارات القيادية والعملية — العمل الجماعي والتواصل واتخاذ القرار والقيادة والمناصرة.",
                     "تعزيز التفكير النقدي — شجّعت النقاشات التفاعلية الطلبة على تحليل القضايا وتقدير وجهات النظر المختلفة واتخاذ قرارات مستنيرة.",
                     "زيادة الانخراط المجتمعي — أصبح الطلبة يرون أنفسهم مشاركين فاعلين في مجتمعاتهم.",
                     "تعزيز القدرات القيادية الشابة عبر الجمع بين التدريب القيادي والتثقيف الحقوقي ومهارات المناصرة.",
                 ])),
]

# --------------------------------------------------------------------------
# 2024 annual report
# --------------------------------------------------------------------------
REPORT_2024 = {
    "en": dict(
        year="2024", title="Annual Report 2024",
        lead="Strategic directions, activities delivered, key outputs and recommendations for 2024.",
        summary_title="Strategic directions",
        summary=[
            "During 2024, HDIP focused on inclusive community development, with particular attention to women, "
            "youth, students and underserved groups. Its work emphasised health education, education support, "
            "research, capacity building and community empowerment.",
            "The programme gave increasing attention to health education as one of the basic pillars for improving "
            "quality of life and strengthening community awareness, delivering awareness programmes on mental "
            "health, reproductive health, sound nutrition and the prevention of chronic disease — through "
            "interactive workshops in schools and universities and media campaigns on social platforms.",
            "2024 was a distinct stage in the programme's path: it continued its leading role in supporting women, "
            "youth and school and university students, using empowerment as a tool for change, education as a means "
            "of advancement, and policy as a route towards social justice.",
        ],
        pillars_title="The five pillars of 2024",
        pillars=[
            ("Health Education and Awareness",
             "Health awareness and educational programmes for women, university students and school students; "
             "workshops on mental health, reproductive health, nutrition, disease prevention and healthy "
             "lifestyles; interactive sessions in schools and universities; digital and social media "
             "dissemination; first aid and emergency response training.",
             ["Increased knowledge and awareness of key health issues.",
              "Improved understanding of disease prevention and healthy behaviours.",
              "Strengthened practical skills in first aid and emergency response.",
              "Improved access to reliable and understandable health information."]),
            ("Research and Knowledge Development",
             "Workshops, lectures and seminars on the importance of scientific research; encouraging students, "
             "researchers and academic communities to engage in research and knowledge sharing; dissemination of "
             "information and educational materials related to health and development.",
             ["Increased awareness among students and researchers of the importance of scientific research.",
              "Strengthened research and critical-thinking skills.",
              "Greater engagement with knowledge generation and evidence-based approaches."]),
            ("Local Capacity Building",
             "Specialised training in health education, health systems and preventive approaches; training "
             "community members, particularly women and youth, as informed participants and contributors within "
             "their communities.",
             ["Strengthened knowledge and practical capacities.",
              "Improved health literacy among targeted women and youth.",
              "Increased ability to make informed health-related decisions."]),
            ("Right to Education Programme",
             "Continued implementation of the Right to Education Programme; educational support to students "
             "experiencing learning gaps; activities to strengthen critical thinking and community participation; "
             "integration of public health concepts into non-formal education.",
             ["Supported students in addressing learning gaps and educational challenges.",
              "Strengthened critical-thinking and problem-solving skills.",
              "Enhanced awareness of the relationship between education and health."]),
            ("Community Empowerment and Inclusion",
             "Prioritising women, youth, students and underserved communities in programme design and delivery; "
             "community-based activities responding to identified educational and health needs.",
             ["Increased access to educational and health knowledge among underserved groups.",
              "Strengthened confidence, knowledge and capacity to engage with community issues.",
              "Contributed to stronger community resilience and participation."]),
        ],
        outputs_title="Key outputs",
        outputs=[
            ("Career guidance programmes", "Workshops and dialogue sessions with professionals from various fields, giving students the chance to learn from real experience and explore career paths."),
            ("Creative competitions", "Competitions in writing, arts, innovation and technology, which helped discover and encourage students' talents and build confidence in their abilities."),
            ("Parental participation", "Regular meetings and awareness workshops that strengthened communication between students, families and the organisation, and increased the support available to students."),
            ("Diverse educational content", "Educational videos, articles and interactive materials that made learning more engaging and addressed students' diverse needs."),
            ("Environmental awareness", "Climate change, sustainability and environmental protection integrated into training, alongside clean-up campaigns and tree-planting initiatives."),
            ("Study groups and research clubs", "Peer study groups for cooperation and mutual academic support, plus a scientific research club established in each library."),
            ("Communication skills", "Workshops that helped students express their ideas, interact with others and build positive relationships with peers."),
            ("Artificial intelligence in education", "AI tools and applications introduced into teaching, including applications supporting language and mathematics learning."),
            ("Reaching underserved groups", "Activities expanded into remote areas, and modern subjects such as programming, digital marketing and digital skills introduced with a focus on women and youth."),
            ("Improving training quality", "Qualified trainers engaged, regular evaluation through questionnaires and participant feedback, psychosocial support sessions, and career consultations."),
        ],
        recs_title="Recommendations",
        recs=[
            ("Expand career guidance programmes", "Cover a wider range of fields and specialisations, with a particular focus on providing students with practical training opportunities."),
            ("Establish an online platform", "Facilitate communication among students, trainers and parents, and support the exchange of information, educational materials and resources."),
            ("Increase cultural and artistic activities", "Enhance cultural awareness and help students understand the importance and role of the arts in society."),
            ("Strengthen volunteer activities", "Build students' sense of social responsibility and develop leadership, communication and teamwork skills."),
            ("Launch targeted training programmes", "Programmes specifically for women with disabilities and unemployed youth, focused on building skills and improving employment opportunities."),
            ("Focus on empowering marginalised groups", "Continue prioritising programmes that improve access to education, training, health and development opportunities."),
            ("Establish a permanent coordination mechanism", "Between civil society organisations and government institutions, to ensure sustained cooperation and coordination of effort."),
            ("Organise annual forums", "To exchange experience, knowledge and best practice among organisations working in development and health."),
        ],
    ),
    "ar": dict(
        year="2024", title="التقرير السنوي 2024",
        lead="التوجهات الاستراتيجية والأنشطة المنفذة وأبرز المخرجات والتوصيات لعام 2024.",
        summary_title="التوجهات الاستراتيجية",
        summary=[
            "خلال عام 2024، ركّزنا على تعزيز التنمية المجتمعية الشاملة، مكثّفين جهودنا على تمكين الفئات المهمّشة، "
            "وخاصة النساء والشباب. وقد انطلقت أنشطتنا من إيمان راسخ بأن النهوض بالمجتمع الفلسطيني لا يمكن تحقيقه "
            "إلا من خلال تمكين أفراده عبر مجالات الصحة والتعليم والتمكين.",
            "أولى البرنامج اهتمامًا متزايدًا بالتثقيف الصحي كأحد الركائز الأساسية لتحسين جودة الحياة وتعزيز الوعي "
            "المجتمعي، فنفّذ سلسلة من البرامج التوعوية التي ركّزت على الصحة النفسية والصحة الإنجابية والتغذية "
            "السليمة والوقاية من الأمراض المزمنة، عبر ورش تفاعلية في المدارس والجامعات وحملات إعلامية على منصات "
            "التواصل الاجتماعي.",
            "لقد شكّل عام 2024 محطة نوعية في مسيرة البرنامج، حيث واصل أداء دوره الريادي في دعم النساء والشباب "
            "وطلاب المدارس والجامعات، مستخدمًا التمكين كأداة للتغيير، والتعليم كوسيلة للنهضة، والسياسات كمسار نحو "
            "العدالة الاجتماعية.",
        ],
        pillars_title="ركائز عام 2024 الخمس",
        pillars=[
            ("التثقيف والتوعية الصحية",
             "برامج توعية وتثقيف صحي للنساء وطلبة الجامعات وطلبة المدارس؛ ورش حول الصحة النفسية والصحة الإنجابية "
             "والتغذية والوقاية من الأمراض وأنماط الحياة الصحية؛ جلسات تفاعلية في المدارس والجامعات؛ النشر عبر "
             "المنصات الرقمية؛ تدريبات الإسعاف الأولي والاستجابة للطوارئ.",
             ["زيادة معرفة المشاركين ووعيهم بالقضايا الصحية الأساسية.",
              "تحسين فهم الوقاية من الأمراض والسلوكيات الصحية.",
              "تعزيز المهارات العملية في الإسعاف الأولي والاستجابة للطوارئ.",
              "تحسين الوصول إلى معلومات صحية موثوقة ومفهومة."]),
            ("البحث وتطوير المعرفة",
             "ورش عمل ومحاضرات وندوات حول أهمية البحث العلمي؛ تشجيع الطلبة والباحثين والمجتمع الأكاديمي على "
             "الانخراط في البحث وتبادل المعرفة؛ نشر المعلومات والمواد التعليمية المتعلقة بالصحة والتنمية.",
             ["زيادة الوعي لدى الطلبة والباحثين بأهمية البحث العلمي.",
              "تعزيز مهارات البحث والتفكير النقدي.",
              "انخراط أكبر في إنتاج المعرفة والمقاربات القائمة على الأدلة."]),
            ("بناء القدرات المحلية",
             "تدريب متخصص في التثقيف الصحي وإدارة النظم الصحية والمقاربات الوقائية؛ تدريب أفراد المجتمع، وخاصة "
             "النساء والشباب، ليكونوا مشاركين واعين ومساهمين في مجتمعاتهم.",
             ["تعزيز المعرفة والقدرات العملية لدى المشاركين.",
              "تحسين الثقافة الصحية لدى النساء والشباب المستهدفين.",
              "زيادة القدرة على اتخاذ قرارات صحية مستنيرة."]),
            ("برنامج الحق في التعليم",
             "استمرار تنفيذ برنامج الحق في التعليم؛ دعم تعليمي للطلبة الذين يعانون من فجوات تعليمية؛ أنشطة لتعزيز "
             "التفكير النقدي والمشاركة المجتمعية؛ إدماج مفاهيم الصحة العامة ضمن التعليم غير الرسمي.",
             ["دعم الطلبة في معالجة الفاقد التعليمي والتحديات التعليمية.",
              "تعزيز مهارات التفكير النقدي وحل المشكلات.",
              "زيادة وعي الطلبة بالعلاقة بين التعليم والصحة."]),
            ("التمكين المجتمعي والشمول",
             "إعطاء الأولوية للنساء والشباب والطلبة والمجتمعات المهمّشة في تصميم البرامج وتنفيذها؛ أنشطة مجتمعية "
             "تستجيب للاحتياجات التعليمية والصحية المحددة.",
             ["زيادة وصول الفئات المهمّشة إلى المعرفة التعليمية والصحية.",
              "تعزيز ثقة المشاركين ومعرفتهم وقدرتهم على الانخراط في قضايا مجتمعهم.",
              "المساهمة في تعزيز صمود المجتمع ومشاركته."]),
        ],
        outputs_title="أبرز المخرجات",
        outputs=[
            ("برامج التوجيه المهني", "ورش عمل وجلسات حوارية مع مهنيين من مجالات متنوعة، أتاحت للطلبة التعلّم من تجارب واقعية واستكشاف مساراتهم المهنية."),
            ("المسابقات الإبداعية", "مسابقات في الكتابة والفنون والابتكار والتكنولوجيا، أسهمت في اكتشاف مواهب الطلبة وتشجيعها وبناء ثقتهم بقدراتهم."),
            ("مشاركة أولياء الأمور", "اجتماعات دورية وورش توعوية عزّزت التواصل بين الطلبة وأسرهم والمؤسسة، وزادت الدعم المتاح للطلبة."),
            ("محتوى تعليمي متنوع", "مقاطع فيديو تعليمية ومقالات وموارد تفاعلية جعلت التعلّم أكثر جاذبية ولبّت احتياجات الطلبة المتنوعة."),
            ("الوعي البيئي", "إدماج التغير المناخي والاستدامة وحماية البيئة في التدريبات، إلى جانب حملات النظافة ومبادرات زراعة الأشجار."),
            ("مجموعات الدعم وأندية البحث", "مجموعات دعم دراسية للتعاون والمساندة الأكاديمية، إضافة إلى نادٍ للبحث العلمي في كل مكتبة."),
            ("مهارات التواصل", "ورش ساعدت الطلبة على التعبير عن أفكارهم والتفاعل مع الآخرين وبناء علاقات إيجابية مع زملائهم."),
            ("الذكاء الاصطناعي في التعليم", "إدخال أدوات وتطبيقات الذكاء الاصطناعي في العملية التعليمية، منها تطبيقات تدعم تعلّم اللغات والرياضيات."),
            ("الوصول إلى الفئات المهمّشة", "توسيع الأنشطة لتشمل المناطق النائية، وإدخال مواضيع حديثة مثل البرمجة والتسويق الرقمي والمهارات الرقمية مع التركيز على النساء والشباب."),
            ("تحسين جودة التدريب", "الاستعانة بمدربين متخصصين، وتقييمات دورية عبر الاستبيانات وملاحظات المشاركين، وجلسات دعم نفسي واجتماعي، واستشارات مهنية."),
        ],
        recs_title="التوصيات",
        recs=[
            ("توسيع برامج التوجيه المهني", "لتشمل المزيد من المجالات والتخصصات، مع التركيز على توفير فرص تدريبية عملية للطلاب."),
            ("إنشاء منصة إلكترونية", "لتسهيل التواصل بين الطلاب والمدربين وأولياء الأمور، ودعم تبادل المعلومات والمواد والموارد."),
            ("زيادة الأنشطة الثقافية والفنية", "لتعزيز الوعي الثقافي وتعليم الطلاب أهمية الفنون ودورها في المجتمع."),
            ("تعزيز الأنشطة التطوعية", "لتعزيز روح المسؤولية الاجتماعية لدى الطلاب وتطوير مهارات القيادة والتواصل والعمل الجماعي."),
            ("إطلاق برامج تدريبية موجّهة", "تستهدف النساء ذوات الإعاقة والشباب العاطلين عن العمل، وتركّز على بناء مهاراتهم وتحسين فرص عملهم."),
            ("التركيز على تمكين الفئات المهمّشة", "مواصلة إعطاء الأولوية للبرامج التي تحسّن وصولهم إلى فرص التعليم والتدريب والصحة والتنمية."),
            ("إنشاء آلية تنسيق دائمة", "بين المؤسسات الأهلية والحكومية لضمان استدامة التعاون وتنسيق الجهود."),
            ("تنظيم منتديات سنوية", "لتبادل الخبرات والمعرفة وأفضل الممارسات بين الجهات العاملة في التنمية والصحة."),
        ],
    ),
}

# --------------------------------------------------------------------------
# News articles — single activities drawn out of the 2024 reports
# --------------------------------------------------------------------------
NEWS = [
    dict(slug="first-aid-2024", photo="women-able-session", area="health", project=None, date="2024",
         en=dict(title="85 first aid courses reach 1,700 students across seven governorates",
                 tag="Health", date="2024",
                 summary="Theoretical and practical training on responding to emergencies — wounds, bleeding, "
                         "fractures, burns, choking, fainting and CPR.",
                 body=["HDIP implemented 85 first aid training courses during 2024, benefiting 1,700 male and "
                       "female students in Hebron, Bethlehem, Abu Dis, Ramallah, Jenin, Tulkarm and Nablus.",
                       "The courses included both theoretical and practical training on how to respond to emergency "
                       "situations, including wounds, bleeding, fractures, burns, choking, fainting and "
                       "cardiopulmonary resuscitation.",
                       "A special course was also organised for students at Birzeit University entitled “How to "
                       "Become a Successful Health-Literate Person”, attended by 20 students.",
                       "Alongside these, 24 emergency first aid courses were delivered across eight areas, focused "
                       "on providing first aid in emergency situations including injuries resulting from shelling "
                       "or military incursions, covering techniques such as controlling bleeding and managing "
                       "fractures."]),
         ar=dict(title="85 دورة إسعاف أولي تصل إلى 1,700 طالب وطالبة في سبع محافظات",
                 tag="الصحة", date="2024",
                 summary="تدريب نظري وعملي على التعامل مع حالات الطوارئ — الجروح والنزيف والكسور والحروق "
                         "والاختناق والإغماء وإنعاش القلب.",
                 body=["نفّذ البرنامج 85 دورة إسعاف أولي خلال عام 2024، استفاد منها 1,700 طالب وطالبة في الخليل "
                       "وبيت لحم وأبو ديس ورام الله وجنين وطولكرم ونابلس.",
                       "تضمّنت هذه الدورات تدريبًا عمليًا ونظريًا على كيفية التعامل مع حالات الطوارئ مثل الجروح "
                       "والنزيف والكسور والحروق والاختناق والإغماء وإنعاش القلب.",
                       "كما تم تنظيم دورة خاصة لطلاب جامعة بيرزيت بعنوان «كيف تكون مثقفًا صحيًا ناجحًا» حضرها "
                       "20 طالبًا وطالبة.",
                       "وإلى جانب ذلك، نُفّذت 24 دورة إسعاف أولي في حالات الطوارئ في ثماني مناطق، ركّزت على تقديم "
                       "الإسعافات في حالات الطوارئ مثل الإصابات الناتجة عن القصف أو الاجتياحات، وشملت تقنيات وقف "
                       "النزيف والتعامل مع الكسور."])),

    dict(slug="first-aid-children-jenin", photo="women-leaders-training", area="health", project=None, date="2024",
         en=dict(title="First aid for children injured during incursions — two courses in Jenin",
                 tag="Health", date="2024",
                 summary="45 women trained in how to treat children wounded during military incursions, using "
                         "techniques suited to children's psychological and physical needs.",
                 body=["Two courses were implemented for 45 women in Jenin, focusing on how to provide first aid to "
                       "children who sustain injuries during military incursions and conflict situations.",
                       "The training emphasised appropriate techniques that take into consideration children's "
                       "specific psychological and physical needs.",
                       "The courses sit within HDIP's wider 2024 health education work, which also included 12 "
                       "women's mental health courses for 210 women covering basic concepts of mental health, "
                       "stress management, coping with anxiety and depression, and psychological support for women "
                       "during pregnancy and childbirth."]),
         ar=dict(title="الإسعافات الأولية للأطفال المصابين أثناء الاجتياحات — دورتان في جنين",
                 tag="الصحة", date="2024",
                 summary="تدريب 45 سيدة على كيفية إسعاف الأطفال المصابين أثناء الاجتياحات، بتقنيات تراعي "
                         "احتياجاتهم النفسية والجسدية.",
                 body=["تم تنفيذ دورتين استهدفتا 45 سيدة في جنين، ناقشتا كيفية تقديم الإسعافات الأولية للأطفال "
                       "الذين يتعرضون للإصابات أثناء الاجتياحات وحالات النزاع.",
                       "وركّز التدريب على تقنيات خاصة تناسب احتياجات الأطفال النفسية والجسدية.",
                       "وتندرج الدورتان ضمن عمل البرنامج الأوسع في التثقيف الصحي لعام 2024، الذي شمل أيضًا 12 دورة "
                       "في صحة المرأة النفسية استهدفت 210 سيدة، وتناولت أساسيات الصحة النفسية وإدارة الضغوط "
                       "والتعامل مع القلق والاكتئاب ودعم النساء نفسيًا خلال الحمل والولادة."])),

    dict(slug="closing-conference", photo="conference-closing", area="women", project="women-able", date="2024",
         en=dict(title="More than 200 women and men meet decision-makers at the closing conference",
                 tag="Women's Empowerment", date="2024",
                 summary="The Women Able to Change Society project closed in Ramallah with a conference where "
                         "women told their own success stories.",
                 body=["At the close of the Women Able to Change Society project, a closing conference was held in "
                       "Ramallah where more than 200 women and men met decision-makers.",
                       "The conference gave women a platform to raise their issues and experiences, contributing "
                       "significantly to their empowerment and to strengthening their participation in political "
                       "and social life.",
                       "During the conference women told their own success stories — a source of pride for the "
                       "project. They demonstrated their ability to share their experience and to invite other "
                       "women to take part, reflecting the behavioural change and the positive impact of the "
                       "training and empowerment programmes delivered.",
                       "The project ran for five years across Hebron, Jenin, Tulkarm and Ramallah, working with 35 "
                       "trainees in each governorate and 16 sites per governorate."]),
         ar=dict(title="أكثر من 200 امرأة ورجل يلتقون بصانعي القرار في المؤتمر الختامي",
                 tag="تمكين المرأة", date="2024",
                 summary="اختُتم مشروع نساء قادرات على تغيير المجتمع في رام الله بمؤتمر روت فيه النساء قصص نجاحهن.",
                 body=["في ختام أنشطة مشروع نساء قادرات على تغيير المجتمع، نُظّم مؤتمر ختامي في رام الله التقى فيه "
                       "أكثر من 200 امرأة ورجل بصانعي القرار.",
                       "أتاح هذا المؤتمر للنساء منصة لطرح قضاياهن وتجاربهن، مما أسهم بشكل كبير في تمكينهن وتعزيز "
                       "مشاركتهن في الحياة السياسية والاجتماعية.",
                       "وخلال المؤتمر قامت النساء بسرد قصص نجاحهن، مما كان بمثابة فخر للمشروع. أظهرن قدرتهن على "
                       "مشاركة تجاربهن ودعوة النساء الأخريات لخوض التجربة، بما يعكس التغير السلوكي والأثر الإيجابي "
                       "لبرامج التدريب والتمكين التي نُفّذت.",
                       "استمر المشروع خمسة أعوام في الخليل وجنين وطولكرم ورام الله، بمشاركة 35 متدربة في كل محافظة "
                       "و16 موقعًا في كل محافظة."])),

    dict(slug="gaza-education", photo="youth-training", area="education", project="right-to-education", date="2024",
         en=dict(title="Right to Education reaches students in displacement settings in Gaza",
                 tag="Education", date="2024",
                 summary="345 activities across eight governorates including Gaza, reaching 8,321 participants "
                         "through an emergency-adapted plan.",
                 body=["Despite school closures, violence, displacement and the war on the Gaza Strip, HDIP "
                       "implemented the Right to Education Project in 2024 within a comprehensive emergency plan "
                       "covering eight governorates including Gaza.",
                       "345 activities were delivered — awareness workshops and educational and training courses — "
                       "across the West Bank, Jerusalem and Gaza. Through these activities, supplementary lessons "
                       "were provided to students in displacement tents, helping to ease the effect of the war on "
                       "education and to keep the educational process going.",
                       "More than 8,321 people benefited: 3,232 males (39%) and 5,089 females (61%), including 355 "
                       "persons with disabilities.",
                       "School courses were delivered through 7 centres in the West Bank and 9 centres in Gaza, "
                       "covering English, mathematics, physics, Arabic, computer skills, science and life skills "
                       "for students from grade 7 to grade 11."]),
         ar=dict(title="الحق في التعليم يصل إلى الطلبة في خيم النزوح في غزة",
                 tag="التعليم", date="2024",
                 summary="345 نشاطًا في ثماني محافظات بما فيها غزة، وصلت إلى 8,321 مستفيدًا ضمن خطة طوارئ شاملة.",
                 body=["رغم إغلاق المدارس والعنف والنزوح والحرب على قطاع غزة، نفّذ البرنامج مشروع الحق في التعليم "
                       "في عام 2024 ضمن خطة طوارئ شاملة في ثماني محافظات بما فيها قطاع غزة.",
                       "بلغ عدد الأنشطة المنفذة 345 فعالية، تنوعت بين ورش عمل ودورات تدريبية، استهدفت محافظات الضفة "
                       "الغربية والقدس وقطاع غزة. ومن خلال هذه الأنشطة تم تقديم دروس تقوية للطلاب في خيم النزوح، "
                       "مما ساعد في تخفيف آثار الحرب على التعليم وضمان استمرار العملية التعليمية.",
                       "استفاد من هذه الأنشطة أكثر من 8,321 مستفيدًا ومستفيدة، شكّل الذكور 39% (3,232 مشاركًا) "
                       "والإناث 61% (5,089 مشاركة)، كما شملت الأنشطة 355 شخصًا من ذوي الإعاقة.",
                       "نُفّذت دورات المدارس عبر 7 مراكز في الضفة الغربية و9 مراكز في غزة، وشملت اللغة الإنجليزية "
                       "والرياضيات والفيزياء واللغة العربية والحاسوب والعلوم والمهارات الحياتية للصفوف من السابع "
                       "حتى الحادي عشر."])),

    dict(slug="ai-and-creativity", photo="women-able-group", area="education", project=None, date="2024",
         en=dict(title="AI tools, creative competitions and research clubs enter the classroom",
                 tag="Education", date="2024",
                 summary="Among 2024's key outputs: AI applications supporting language and mathematics learning, "
                         "creative competitions, and a scientific research club in every library.",
                 body=["A number of artificial intelligence tools and applications were introduced into the "
                       "educational process during 2024, including applications that support language and "
                       "mathematics learning. This contributed to more interactive learning methods and encouraged "
                       "students to use technology to develop their skills.",
                       "A series of creative competitions was organised in writing, arts, innovation and "
                       "technology. These contributed to discovering and encouraging students' talents, fostering "
                       "creativity and positive competition, and strengthening students' confidence in their "
                       "abilities.",
                       "Study support groups were formed among students to promote cooperation, knowledge sharing "
                       "and mutual academic assistance. In addition, a scientific research club was established in "
                       "each library to encourage students to conduct research and inquiry, develop critical "
                       "thinking and foster interest in science and knowledge.",
                       "Topics related to climate change, sustainability and environmental protection were "
                       "integrated into training sessions and workshops, alongside practical activities such as "
                       "clean-up campaigns and tree-planting initiatives."]),
         ar=dict(title="أدوات الذكاء الاصطناعي والمسابقات الإبداعية وأندية البحث تدخل الصف",
                 tag="التعليم", date="2024",
                 summary="من أبرز مخرجات 2024: تطبيقات ذكاء اصطناعي تدعم تعلّم اللغات والرياضيات، ومسابقات "
                         "إبداعية، ونادٍ للبحث العلمي في كل مكتبة.",
                 body=["تم إدخال عدد من أدوات وتطبيقات الذكاء الاصطناعي في العملية التعليمية خلال عام 2024، منها "
                       "تطبيقات تساعد في تعلّم اللغات والرياضيات. وقد ساهم ذلك في توفير أساليب تعلّم أكثر تفاعلية "
                       "وشجّع الطلبة على استخدام التكنولوجيا لتطوير مهاراتهم.",
                       "ونُظّمت سلسلة من المسابقات الإبداعية في مجالات الكتابة والفنون والابتكار والتكنولوجيا، "
                       "أسفرت عن اكتشاف مواهب جديدة بين الطلبة وزيادة روح المنافسة الإيجابية وتعزيز ثقتهم بقدراتهم.",
                       "كما تم تشكيل مجموعات دعم دراسية بين الطلبة لتعزيز التعاون ومشاركة المعرفة والمساندة "
                       "الأكاديمية، إضافة إلى تشكيل نادٍ للبحث العلمي في كل مكتبة لتشجيع الطلبة على البحث "
                       "والاستقصاء وتطوير مهارات التفكير النقدي.",
                       "وأُدرجت مواضيع تتعلق بالتغير المناخي والاستدامة وحماية البيئة ضمن التدريبات وورشات العمل، "
                       "إلى جانب فعاليات عملية مثل أيام النظافة وزراعة الأشجار."])),
]

# --------------------------------------------------------------------------
# Contact
# --------------------------------------------------------------------------
CONTACT = {
    "en": dict(
        title="Contact & partnership",
        lead="HDIP works with local and international partners on research, training, evaluation and community "
             "programmes. Write to us about a partnership, a consultation or access to our reporting.",
        details_title="Contact details",
        unverified="These details are carried over from HDIP's earlier published site and need confirmation.",
        partners_title="Partners",
        partners_lead="Two partners are identifiable from the 2024 programme photographs. A full donor and partner "
                      "list, with logos we may display, has not been supplied.",
        partners=[("Friedrich-Ebert-Stiftung", "Young Leadership in Universities"),
                  ("Olof Palme International Center", "Women Able to Change Society")],
        direct_title="Get in touch",
        direct_lead="Write to us directly and we will route your message to the right unit. "
                    "For partnership and consultancy enquiries, please include the programme "
                    "area and the timeframe you are working to.",
        email_cta="Email HDIP", call_cta="Call the office",
    ),
    "ar": dict(
        title="التواصل والشراكة",
        lead="يعمل البرنامج مع شركاء محليين ودوليين في البحث والتدريب والتقييم والبرامج المجتمعية. راسلنا بشأن "
             "شراكة أو استشارة أو للاطلاع على تقاريرنا.",
        details_title="بيانات الاتصال",
        unverified="هذه البيانات منقولة عن الموقع المنشور سابقًا وبحاجة إلى تأكيد.",
        partners_title="الشركاء",
        partners_lead="يمكن تمييز شريكين من صور برامج عام 2024. ولم يتم تزويدنا بقائمة كاملة بالممولين والشركاء "
                      "والشعارات المسموح بعرضها.",
        partners=[("مؤسسة فريدريش إيبرت", "تعزيز القيادات الشابة في الجامعات"),
                  ("مركز أولوف بالمه الدولي", "نساء قادرات على تغيير المجتمع")],
        direct_title="تواصل معنا",
        direct_lead="راسلنا مباشرة وسنحوّل رسالتك إلى الوحدة المعنية. وللاستفسارات المتعلقة "
                    "بالشراكة والاستشارات، يُرجى ذكر المجال البرامجي والإطار الزمني الذي تعملون ضمنه.",
        email_cta="راسلنا بالبريد", call_cta="اتصل بالمكتب",
    ),
}

CONTACT_FIELDS = [
    ("pin", "Address", "العنوان", "PO Box 1351<br>Ramallah, Palestine", "ص.ب 1351<br>رام الله، فلسطين", None),
    ("phone", "Telephone", "الهاتف", "+972 2 298 5372", "+972 2 298 5372", "tel:+97222985372"),
    ("print", "Fax", "الفاكس", "+972 2 298 5917", "+972 2 298 5917", None),
    ("mail", "Email", "البريد الإلكتروني", "hdip@hdip.org", "hdip@hdip.org", "mailto:hdip@hdip.org"),
]
