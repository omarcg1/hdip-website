#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-year content: 2022, 2023, 2024 and 2025.

Sources (all supplied by HDIP):
  2022  HDIP Narative report 2022.docx (EN)
  2023  Program During 2023.docx (EN)
  2024  the 2024 batch — see content.SOURCES
  2025  Our Strategic Directions / Key Achievements / Health Activities /
        General Recommendations / the four project files (EN),
        with Arabic counterparts توجهاتنا خلال عام 2025 / أبرز مخرجات عام 2025 /
        الأنشطة والبرامج الصحية في 2025 / التوصيات العامة / four project files
  profile  Health Development Information and Policy Institute.docx (EN)

The 2023 figures carry a caveat — see REPORTS["2023"]["caveat"].
"""

SOURCES_EXTRA = {
    "profile_en": "Health Development Information and Policy Institute.docx — English profile (EN)",
    "narrative22": "HDIP Narative report 2022.docx — objectives, 2022 directions, libraries (EN)",
    "program23": "Program During 2023.docx — 2023 directions, health, projects, statistics (EN)",
    "directions25": "Our Strategic Directions in 2025.docx / توجهاتنا خلال عام 2025.docx",
    "achievements25": "Key Achievements and Results in 2025.docx / أبرز مخرجات عام 2025.docx",
    "health25": "Health Activities and Programs in 2025.docx / الأنشطة والبرامج الصحية في 2025.docx",
    "recs25": "General Recommendations.docx / التوصيات العامة.docx",
    "projects25": "Right to Education / Women Able / Women Leaders / Young Leadership (EN + AR)",
}

YEARS = ["2025", "2024", "2023", "2022"]

# --------------------------------------------------------------------------
# Homepage "Impact in numbers" — one set per year, switchable
# --------------------------------------------------------------------------
IMPACT = {
    "2025": [
        dict(num="11,500+", en="direct beneficiaries across all programmes",
             ar="مستفيدًا مباشرًا من مجمل البرامج"),
        dict(num="1,460", en="students trained in first aid across 73 courses",
             ar="طالبًا وطالبة في 73 دورة إسعاف أولي"),
        dict(num="3,216", en="students in intensive remedial classes in Gaza",
             ar="طالبًا في دورات تعويضية مكثفة في غزة"),
        dict(num="181", en="employment opportunities created",
             ar="فرصة عمل تم إيجادها"),
    ],
    "2024": [
        dict(num="8,321", en="participants in the Right to Education Project, 61% female",
             ar="مستفيدًا في مشروع الحق في التعليم، 61% إناث"),
        dict(num="345", en="activities delivered across eight governorates",
             ar="نشاطًا في ثماني محافظات"),
        dict(num="1,700", en="students trained in first aid across 85 courses",
             ar="طالبًا وطالبة في 85 دورة إسعاف أولي"),
        dict(num="355", en="participants with disabilities included",
             ar="مشاركًا من ذوي الإعاقة"),
    ],
    "2023": [
        dict(num="2,130", en="students reached across 78 education activities",
             ar="طالبًا في 78 نشاطًا تعليميًا"),
        dict(num="2,000", en="participants in 222 health awareness workshops",
             ar="مشاركًا في 222 ورشة توعية صحية"),
        dict(num="200", en="people trained to deliver health education in their own communities",
             ar="شخصًا تدربوا على التثقيف الصحي في مجتمعاتهم"),
        dict(num="7", en="universities in the Student in Need Fund campaign",
             ar="جامعات في حملة صندوق الطالب المحتاج"),
    ],
    "2022": [
        dict(num="40,200", en="books across eight community knowledge libraries",
             ar="كتابًا في ثماني مكتبات مجتمعية"),
        dict(num="1,920", en="students reached through 230 training courses",
             ar="طالبًا عبر 230 دورة تدريبية"),
        dict(num="43", en="graduation projects and theses supported",
             ar="مشروع تخرج ورسالة ماجستير بدعم من المكتبات"),
        dict(num="80", en="student volunteers running the libraries",
             ar="متطوعًا جامعيًا يديرون المكتبات"),
    ],
}

# --------------------------------------------------------------------------
# About — the English profile fills the three gaps flagged earlier
# --------------------------------------------------------------------------
ABOUT_EXTRA = {
    "en": dict(
        whatwedo_title="What we do",
        whatwedo_lead="HDIP works across seven interconnected areas. Five of them are presented on this "
                      "site as programme areas with their own pages.",
        whatwedo=[
            ("Health and Health Education", "Promoting health awareness, prevention, healthy behaviours, mental health, and access to reliable health information.", "health"),
            ("Education and Youth Development", "Supporting students through educational programmes, training, mentoring, community libraries, skills development and access to learning opportunities.", "education"),
            ("Women's Empowerment", "Developing programmes that strengthen women's knowledge, skills, participation, resilience and access to economic and social opportunities.", "women"),
            ("Community Development", "Working with local communities and institutions to identify needs and develop practical, sustainable responses.", None),
            ("Research, Policy and Advocacy", "Conducting research, assessments and policy-oriented activities that generate evidence and support informed decision-making.", "research"),
            ("Capacity Building", "Providing training and technical support to individuals, civil society organisations and local institutions.", "youth"),
            ("Monitoring, Evaluation and Learning", "Applying systematic approaches to monitoring implementation, measuring results, documenting lessons and improving programme quality.", None),
        ],
        approach_title="Our approach",
        approach=[
            "HDIP places people and communities at the centre of development. Our programmes are designed "
            "based on identified needs and implemented through participatory approaches that encourage "
            "local ownership and meaningful engagement.",
            "We seek to connect research with practical action, ensuring that programme design is informed "
            "by evidence while remaining responsive to the realities faced by communities. We also promote "
            "partnerships and coordination among civil society organisations, educational institutions, "
            "governmental bodies and other stakeholders.",
        ],
        partner_title="Why partner with us",
        partner_lead="HDIP is committed to implementing donor-supported programmes with professionalism, "
                     "transparency, accountability and effective resource management. We value long-term "
                     "partnerships and work closely with donors and implementing partners to ensure that "
                     "agreed objectives, activities, outputs and reporting requirements are met.",
        principles=[
            "Clear and measurable programme objectives and results.",
            "Transparent financial and administrative procedures.",
            "Regular monitoring, documentation and reporting.",
            "Evidence-based programme design and decision-making.",
            "Community participation and stakeholder engagement.",
            "Continuous learning and improvement.",
            "Sustainability and institutional capacity development.",
        ],
        partner_close="With more than three decades of experience, HDIP offers partners a combination of "
                      "local knowledge, technical expertise, community access, programme implementation "
                      "capacity and commitment to accountability. Through collaboration with donors and "
                      "development partners, HDIP seeks to translate resources and knowledge into practical, "
                      "measurable and sustainable benefits for Palestinian communities.",
    ),
    "ar": dict(
        whatwedo_title="ماذا نعمل",
        whatwedo_lead="يعمل البرنامج في سبعة مجالات مترابطة، خمسة منها معروضة على هذا الموقع كمجالات "
                      "برامجية لكل منها صفحتها.",
        whatwedo=[
            ("الصحة والتثقيف الصحي", "تعزيز الوعي الصحي والوقاية والسلوكيات الصحية والصحة النفسية والوصول إلى معلومات صحية موثوقة.", "health"),
            ("التعليم وتنمية الشباب", "دعم الطلبة عبر البرامج التعليمية والتدريب والإرشاد والمكتبات المجتمعية وتنمية المهارات وإتاحة فرص التعلّم.", "education"),
            ("تمكين المرأة", "برامج تعزّز معرفة النساء ومهاراتهن ومشاركتهن وصمودهن ووصولهن إلى الفرص الاقتصادية والاجتماعية.", "women"),
            ("التنمية المجتمعية", "العمل مع المجتمعات والمؤسسات المحلية لتحديد الاحتياجات وتطوير استجابات عملية ومستدامة.", None),
            ("البحث والسياسات والمناصرة", "إجراء البحوث والتقييمات والأنشطة السياساتية التي تنتج الأدلة وتدعم اتخاذ القرار المستنير.", "research"),
            ("بناء القدرات", "تقديم التدريب والدعم الفني للأفراد ومؤسسات المجتمع المدني والمؤسسات المحلية.", "youth"),
            ("المتابعة والتقييم والتعلّم", "اعتماد مقاربات منهجية لمتابعة التنفيذ وقياس النتائج وتوثيق الدروس وتحسين جودة البرامج.", None),
        ],
        approach_title="منهجيتنا",
        approach=[
            "يضع البرنامج الناس والمجتمعات في قلب التنمية. تُصمَّم برامجنا بناءً على احتياجات محددة "
            "وتُنفَّذ بمقاربات تشاركية تشجّع الملكية المحلية والانخراط الحقيقي.",
            "نسعى إلى ربط البحث بالعمل التطبيقي، بما يضمن أن يكون تصميم البرامج قائمًا على الأدلة "
            "ومستجيبًا في الوقت نفسه لواقع المجتمعات. كما نعزّز الشراكات والتنسيق بين مؤسسات المجتمع "
            "المدني والمؤسسات التعليمية والجهات الحكومية وأصحاب المصلحة الآخرين.",
        ],
        partner_title="لماذا الشراكة معنا",
        partner_lead="يلتزم البرنامج بتنفيذ البرامج المدعومة من الممولين بمهنية وشفافية ومساءلة وإدارة "
                     "فعّالة للموارد. ونقدّر الشراكات طويلة الأمد ونعمل عن قرب مع الممولين والشركاء "
                     "المنفذين لضمان تحقيق الأهداف والأنشطة والمخرجات ومتطلبات التقارير المتفق عليها.",
        principles=[
            "أهداف ونتائج برامجية واضحة وقابلة للقياس.",
            "إجراءات مالية وإدارية شفافة.",
            "متابعة وتوثيق وإعداد تقارير بشكل منتظم.",
            "تصميم البرامج واتخاذ القرار استنادًا إلى الأدلة.",
            "مشاركة المجتمع وانخراط أصحاب المصلحة.",
            "التعلّم والتحسين المستمران.",
            "الاستدامة وتطوير القدرات المؤسسية.",
        ],
        partner_close="بخبرة تمتد أكثر من ثلاثة عقود، يوفّر البرنامج لشركائه مزيجًا من المعرفة المحلية "
                      "والخبرة الفنية والوصول المجتمعي وقدرة التنفيذ والالتزام بالمساءلة. ومن خلال التعاون "
                      "مع الممولين وشركاء التنمية، يسعى البرنامج إلى ترجمة الموارد والمعرفة إلى منافع عملية "
                      "وقابلة للقياس ومستدامة للمجتمعات الفلسطينية.",
    ),
}

# --------------------------------------------------------------------------
# Community knowledge libraries — 2022 Narrative Report
# --------------------------------------------------------------------------
LIBRARIES = {
    "en": dict(
        title="Community research and knowledge libraries",
        lead="A continuation of the Supporting Libraries Project in the West Bank and Gaza Strip, providing "
             "academic assistance to students — particularly students in need and students with disabilities.",
        body=[
            "HDIP established eight libraries holding approximately 15,000 books. The collections were later "
            "updated and expanded to roughly 40,200 books, including cultural and scientific books, "
            "references, periodicals, academic textbooks adopted by local universities, and encyclopaedias "
            "across scientific, cultural, social, political, literary and legal fields.",
            "The libraries are managed by a team of eight trained librarians, supported by approximately 80 "
            "university student volunteers who classify and organise books, lend to users, and coordinate "
            "training courses and other activities. They are located across eight Palestinian governorates.",
        ],
        facilities_title="Facilities",
        facilities=[
            "An electronic research room with computers connected to the internet.",
            "Training rooms used for educational activities and documentary screenings.",
            "A systematically and electronically catalogued collection.",
            "Dedicated spaces for reading and research.",
        ],
        services_title="Services",
        services=[
            ("Academic and cultural book lending", "Reducing the financial burden of purchasing textbooks."),
            ("Computer and internet access", "Laboratories for educational and research use."),
            ("Printing and photocopying", "Available to all students."),
            ("Specialised academic and skills courses", "Including empowerment and personal skills development, supporting access to employment after graduation."),
        ],
        figures=[("8", "libraries across eight governorates"), ("40,200", "books"),
                 ("230", "training courses for ~1,920 students"), ("43", "graduation projects supported")],
        workshops_title="Workshops run through the libraries",
        workshops=[
            "Inclusion and integration of persons with disabilities.",
            "Educational policies in Palestine.",
            "The importance of scientific research.",
            "Development of information systems.",
            "Raising awareness about education.",
            "The status and quality of higher education in Palestine.",
            "The role of civil society organisations in educational policies.",
            "Freedom of movement and accessibility of educational institutions for persons with disabilities.",
        ],
    ),
    "ar": dict(
        title="مكتبات البحث والمعرفة المجتمعية",
        lead="استكمالًا لمشروع دعم المكتبات في الضفة الغربية وقطاع غزة، الذي يقدّم المساعدة الأكاديمية "
             "للطلبة، وخاصة الطلبة المحتاجين والطلبة ذوي الإعاقة.",
        body=[
            "أنشأ البرنامج ثماني مكتبات تضم نحو 15,000 كتاب، ثم جرى تحديث المقتنيات وتوسيعها لتبلغ نحو "
            "40,200 كتاب، تشمل كتبًا ثقافية وعلمية ومراجع ودوريات وكتبًا أكاديمية معتمدة في الجامعات "
            "المحلية، إضافة إلى موسوعات علمية وثقافية واجتماعية وسياسية وأدبية وقانونية.",
            "يدير المكتبات فريق من ثمانية أمناء مكتبات مدرَّبين، يدعمهم نحو 80 متطوعًا من طلبة الجامعات "
            "يساعدون في تصنيف الكتب وتنظيمها وإعارتها وتنسيق الدورات التدريبية وغيرها من الأنشطة. "
            "وتنتشر المكتبات في ثماني محافظات فلسطينية.",
        ],
        facilities_title="المرافق",
        facilities=[
            "غرفة بحث إلكتروني مزودة بحواسيب متصلة بالإنترنت.",
            "غرف تدريب تُستخدم للأنشطة التعليمية وعرض الأفلام الوثائقية.",
            "مقتنيات مفهرسة منهجيًا وإلكترونيًا.",
            "مساحات مخصصة للقراءة والبحث.",
        ],
        services_title="الخدمات",
        services=[
            ("إعارة الكتب الأكاديمية والثقافية", "تخفيف العبء المالي لشراء الكتب الدراسية."),
            ("الحواسيب والإنترنت", "مختبرات للاستخدام التعليمي والبحثي."),
            ("الطباعة والتصوير", "متاحة لجميع الطلبة."),
            ("دورات أكاديمية ومهارية متخصصة", "تشمل التمكين وتطوير المهارات الشخصية بما يدعم الوصول إلى فرص العمل بعد التخرج."),
        ],
        figures=[("8", "مكتبات في ثماني محافظات"), ("40,200", "كتاب"),
                 ("230", "دورة تدريبية لنحو 1,920 طالبًا"), ("43", "مشروع تخرج مدعوم")],
        workshops_title="ورش تُنفَّذ عبر المكتبات",
        workshops=[
            "دمج الأشخاص ذوي الإعاقة وإشراكهم.",
            "السياسات التعليمية في فلسطين.",
            "أهمية البحث العلمي.",
            "تطوير نظم المعلومات.",
            "التوعية بأهمية التعليم.",
            "واقع التعليم العالي في فلسطين وجودته.",
            "دور مؤسسات المجتمع المدني في السياسات التعليمية.",
            "حرية الحركة وإتاحة المؤسسات التعليمية للأشخاص ذوي الإعاقة.",
        ],
    ),
}

# --------------------------------------------------------------------------
# Project phases — the "Results by year" tabs in the approved template
# --------------------------------------------------------------------------
PHASES = {
    "right-to-education": {
        "2025": dict(
            en=dict(headline="Two complementary pathways: awareness against dropout, and academic capacity.",
                    notes=["Despite complex field and political challenges the project maintained a high "
                           "level of continuity and strong implementation rates, supported by the "
                           "flexibility of project teams, the competence of trainers, and continuous "
                           "cooperation with schools and universities.",
                           "A second strand, the Right to Education Support Project 2, responded to the "
                           "financial and academic barriers facing students through scholarships, skills "
                           "development, rights-based advocacy and remedial teaching. Implementation rates "
                           "for most targeted results ranged between 95% and 100%."],
                    results=[
                        "100 awareness-raising sessions, producing an 80% increase in participants' awareness of the importance of education.",
                        "3,300 students reached through the general training programme, delivered via 8 centres at 144 training hours per centre.",
                        "3,216 students in the Gaza Strip reached through intensive remedial courses across 67 classes in 3 locations.",
                        "768 students (460 female, 308 male) in workshops on scientific research, technology and life skills.",
                        "200 students from 8 local universities in the Scientific Research Ethics Campaign.",
                        "130 students (96 female, 34 male) received scholarships covering tuition and educational costs, at a 95% implementation rate.",
                        "170 students (45 female, 125 male) in rights-based workshops on the Right to Education.",
                        "1,100 school students in an intensive remedial programme across 34 classes, delivering 3,129 actual teaching hours.",
                        "181 permanent and temporary employment opportunities created for educational and administrative personnel.",
                    ]),
            ar=dict(headline="مساران متكاملان: التوعية للحد من التسرب، وبناء القدرات الأكاديمية.",
                    notes=["رغم التحديات الميدانية والسياسية المعقّدة، حافظ المشروع على مستوى عالٍ من "
                           "الاستمرارية وحقق نسب تنفيذ مرتفعة، بفضل مرونة فرق العمل وكفاءة المدربين "
                           "والتعاون المستمر مع المدارس والجامعات.",
                           "واستجاب مسار ثانٍ، مشروع دعم الحق في التعليم 2، للعوائق المالية والأكاديمية "
                           "التي تواجه الطلبة عبر المنح وتنمية المهارات والمناصرة الحقوقية والتعليم "
                           "التعويضي. وتراوحت نسب التنفيذ لمعظم النتائج المستهدفة بين 95% و100%."],
                    results=[
                        "100 جلسة توعوية أسهمت في زيادة وعي المشاركين بأهمية التعليم بنسبة 80%.",
                        "3,300 طالب وطالبة عبر البرنامج التدريبي العام في 8 مراكز بواقع 144 ساعة تدريبية لكل مركز.",
                        "3,216 طالبًا في قطاع غزة عبر دورات تعويضية مكثفة في 67 صفًا و3 مواقع.",
                        "768 طالبًا (460 إناث و308 ذكور) في ورش البحث العلمي والتكنولوجيا والمهارات الحياتية.",
                        "200 طالب من 8 جامعات محلية في حملة أخلاقيات البحث العلمي.",
                        "130 طالبًا (96 إناث و34 ذكور) حصلوا على منح تغطي الرسوم والتكاليف التعليمية بنسبة تنفيذ 95%.",
                        "170 طالبًا (45 إناث و125 ذكور) في ورش حقوقية وتوعوية حول الحق في التعليم.",
                        "1,100 طالب مدرسة في برنامج تعويضي مكثف عبر 34 صفًا، بواقع 3,129 ساعة تدريس فعلية.",
                        "181 فرصة عمل دائمة ومؤقتة للكوادر التعليمية والإدارية.",
                    ])),
    },
    "women-able": {
        "2025": dict(
            en=dict(headline="Economic empowerment, employment for displaced women, and psychosocial support.",
                    notes=["The 2025 phase added an economic strand, \"Skill and Idea\", and responded to "
                           "displacement in Jenin and Tulkarm by creating paid work for displaced women "
                           "running children's camps."],
                    results=[
                        "100 participants trained in advanced beauty and personal care, digital marketing, photography and design, with workshops on advocacy, social justice and gender equality.",
                        "5 product marketing exhibitions involving 100 beneficiaries (70 women, 30 men), creating direct marketing opportunities and links to civil society and decision-makers.",
                        "14 displaced women employed across a summer camp reaching 160 participants and a winter camp reaching 220.",
                        "A three-day evaluation and psychosocial support workshop — 25 sessions for 25 women, using mindfulness, reflective writing and drawing.",
                        "A three-day winter mental health camp for 25 women from marginalised and displaced communities.",
                        "3 alliance-building activities with 20 local leaders, and 4 roundtables with 40 civil society representatives and decision-makers.",
                        "10 further alliance-building meetings reaching 30 participants, and a concluding training seminar in Ramallah for 52 participants.",
                    ]),
            ar=dict(headline="التمكين الاقتصادي وتشغيل النساء النازحات والدعم النفسي الاجتماعي.",
                    notes=["أضافت مرحلة 2025 مسارًا اقتصاديًا بعنوان «حِرفة وفكرة»، واستجابت لواقع النزوح "
                           "في جنين وطولكرم بإيجاد فرص عمل مأجورة للنساء النازحات في مخيمات الأطفال."],
                    results=[
                        "تدريب 100 مشارك ومشاركة على التجميل المتقدم والعناية الشخصية والتسويق الرقمي والتصوير والتصميم، مع ورش في المناصرة والعدالة الاجتماعية والمساواة الجندرية.",
                        "5 معارض لتسويق منتجات النساء بمشاركة 100 مستفيد (70 امرأة و30 رجلًا)، أتاحت فرص تسويق مباشرة وتشبيكًا مع المجتمع المدني وصانعي القرار.",
                        "تشغيل 14 امرأة نازحة في مخيم صيفي استهدف 160 مشاركًا ومخيم شتوي استهدف 220.",
                        "ورشة تقييم ودعم نفسي اجتماعي على مدار ثلاثة أيام — 25 جلسة لـ25 سيدة، باستخدام اليقظة الذهنية والكتابة التأملية والرسم.",
                        "مخيم شتوي متخصص في الصحة النفسية على مدار ثلاثة أيام لـ25 سيدة من المجتمعات المهمّشة والنازحة.",
                        "3 أنشطة لبناء التحالفات بمشاركة 20 قياديًا محليًا، و4 موائد مستديرة بمشاركة 40 من ممثلي المجتمع المدني وصانعي القرار.",
                        "10 لقاءات إضافية لبناء التحالفات استهدفت 30 مشاركًا، وندوة تدريبية ختامية في رام الله بمشاركة 52 شخصًا.",
                    ])),
    },
    "women-leaders": {
        "2025": dict(
            en=dict(headline="A 30-hour intensive structured around four components.",
                    notes=["The training brought together women activists and women interested in running "
                           "for office, from different geographic and marginalised areas."],
                    results=[
                        "Political and knowledge component: the legal and institutional framework, and the mechanics of local elections under applicable Palestinian law.",
                        "Leadership and communication: tools for influence, leadership, effective communication and building cross-sectoral alliances.",
                        "Campaign management and planning: developing an electoral platform, managing resources and media messaging.",
                        "Experience-sharing and networking: direct meetings with former women leaders.",
                        "A noticeable improvement in participants' political and legal awareness and their capacity to analyse political issues.",
                        "A number of participants expressed their intention to run for leadership positions in their local councils.",
                    ]),
            ar=dict(headline="تدريب مكثف من 30 ساعة مبني على أربعة مكوّنات.",
                    notes=["جمع التدريب ناشطات ونساء مهتمات بالترشح للانتخابات من مناطق جغرافية مختلفة "
                           "ومن مجتمعات مهمّشة."],
                    results=[
                        "المكوّن السياسي والمعرفي: الإطار القانوني والمؤسسي وآليات الانتخابات المحلية وفق القوانين والأنظمة الفلسطينية السارية.",
                        "مكوّن القيادة والاتصال: أدوات التأثير والقيادة والتواصل الفعّال وبناء التحالفات المجتمعية والسياسية العابرة للقطاعات.",
                        "مكوّن إدارة الحملات والتخطيط: التطبيق العملي لإدارة الحملة الانتخابية من بناء البرنامج الانتخابي إلى إدارة الموارد والرسائل الإعلامية.",
                        "مكوّن تبادل الخبرات والتشبيك: لقاءات مباشرة مع قياديات سابقات لتبادل التجارب والدروس والاستراتيجيات العملية.",
                        "تحسّن ملحوظ في الوعي السياسي والقانوني لدى المشاركات وقدرتهن على تحليل القضايا السياسية.",
                        "عبّر عدد من المشاركات عن نيتهن الترشح لمواقع قيادية في مجالسهن المحلية.",
                    ])),
    },
    "youth-leadership": {
        "2025": dict(
            en=dict(headline="A 30-hour intensive across democratic leadership, human rights and advocacy.",
                    notes=["Delivered over three consecutive days of focused programme activity."],
                    results=[
                        "Democratic leadership: participatory approaches, collective leadership, and respect for diversity and pluralism.",
                        "Human rights and the international framework: fundamental rights, international instruments, and mechanisms for promoting and defending them.",
                        "Advocacy and campaigning: strategic planning skills and practical tools for designing and running campaigns.",
                        "Strengthened critical and analytical thinking, supporting more informed decision-making.",
                        "Increased self-confidence alongside noticeable improvement in academic engagement and performance.",
                        "Expanded social and professional networks across universities, overcoming geographic separation between campuses.",
                        "Improved employability skills — time management, leadership, communication, negotiation and teamwork.",
                    ]),
            ar=dict(headline="تدريب مكثف من 30 ساعة في القيادة الديمقراطية وحقوق الإنسان والمناصرة.",
                    notes=["نُفِّذ على مدار ثلاثة أيام متتالية من الأنشطة البرامجية المركّزة."],
                    results=[
                        "القيادة الديمقراطية: المقاربات التشاركية وترسيخ مبادئ القيادة الجماعية واحترام التنوع والتعددية.",
                        "حقوق الإنسان والإطار الدولي: الحقوق الأساسية والمواثيق الدولية وآليات تعزيزها والدفاع عنها.",
                        "المناصرة والحملات: مهارات التخطيط الاستراتيجي وأدوات عملية لتصميم حملات المناصرة وتنفيذها.",
                        "تعزيز التفكير النقدي والتحليلي بما يدعم اتخاذ قرارات أكثر استنارة.",
                        "زيادة الثقة بالنفس مع تحسّن ملحوظ في الانخراط والأداء الأكاديمي.",
                        "توسيع الشبكات الاجتماعية والمهنية بين الجامعات وتجاوز الفصل الجغرافي بين الحرم الجامعية.",
                        "تحسين مهارات التوظيف — إدارة الوقت والقيادة والتواصل والتفاوض والعمل الجماعي.",
                    ])),
    },
}

# --------------------------------------------------------------------------
# Annual reports 2022, 2023, 2025 (2024 lives in content.REPORT_2024)
# --------------------------------------------------------------------------
REPORTS = {
    "2025": {
        "en": dict(
            year="2025", title="Annual Report 2025",
            lead="Strategic directions, achievements, results and recommendations for 2025.",
            summary_title="Strategic directions",
            summary=[
                "Throughout 2025, our strategy focused on advancing community development by directing our "
                "efforts and resources toward unlocking the potential of groups most in need of support, "
                "particularly young people and women. These interventions reflected our firm belief that "
                "the progress and prosperity of Palestinian society are closely linked to empowering its "
                "vital pillars across four interconnected areas: health, education, empowerment and "
                "self-reliance.",
            ],
            pillars_title="Four strategic directions",
            pillars=[
                ("A development vision for comprehensive community empowerment",
                 "HDIP positioned health education and awareness as a key pillar for improving public health "
                 "and strengthening community awareness, delivering awareness and educational programmes "
                 "through interactive sessions and discussion forums in academic institutions and schools, "
                 "complemented by digital campaigns on social media.",
                 ["Promoting mental health and community resilience.",
                  "Increasing awareness of reproductive health and family well-being.",
                  "Promoting healthy nutrition and healthy lifestyle practices.",
                  "Strengthening prevention and reducing the spread and impact of chronic diseases."]),
                ("Women's economic empowerment and vocational skills development",
                 "Recognising women's economic independence as a foundation for resilient communities, HDIP "
                 "ran specialised workshops and courses in areas with growing demand in the local market, "
                 "going beyond technical skill into small-business management, entrepreneurship and "
                 "innovation.",
                 ["Beauty and hairdressing — practical skills for small businesses or employment.",
                  "Photography and digital production — visual content skills opening freelance pathways.",
                  "Resin crafts and handicrafts — creativity combined with income generation."]),
                ("Strengthening scientific research and the academic environment",
                 "HDIP positioned scientific research as a pathway for strengthening education, leading "
                 "specialised seminars, awareness lectures and interactive workshops.",
                 ["Encouraging researchers and emerging academics to adopt sound research methodologies.",
                  "Strengthening community awareness of research as a tool for knowledge generation.",
                  "Supporting evidence-based learning and the addressing of strategic challenges."]),
                ("Advancing knowledge integration through the Right to Education projects",
                 "HDIP continued to implement and manage the Right to Education project as a practical model "
                 "for integrating educational and awareness-raising interventions.",
                 ["Addressing learning gaps resulting from exceptional and challenging circumstances.",
                  "Promoting critical thinking, problem-solving and positive community engagement.",
                  "Incorporating public health concepts into non-formal and extracurricular learning."]),
            ],
            outputs_title="Key achievements and results",
            outputs=[
                ("Health activities and programmes", "73 first aid courses for 1,460 students; 8 women's mental health courses for 160 women; 6 health education workshops for 420 students — approximately 2,040 direct beneficiaries from the main health activities."),
                ("Women Able to Change Society", "4 governorates through 16 local sites; 100 participants in \"Skill and Idea\" training; 5 product exhibitions with 100 beneficiaries; 14 displaced women employed across two children's camps reaching 380; 50 women in evaluation, psychosocial support and a winter mental health camp; 12 coordination meetings, 10 alliance-building meetings, 4 roundtables and a concluding seminar for 52."),
                ("Right to Education and its components", "100 awareness sessions producing an 80% rise in awareness; 3,300 students through 8 centres; 3,216 students in Gaza through 67 remedial classes; 768 students in research, technology and life-skills workshops; 200 students from 8 universities in the research ethics campaign; 130 scholarships; 170 students in rights-based workshops; 1,100 school students across 34 remedial classes; 181 employment opportunities created."),
                ("Women Leaders in Local Councils", "A 30-hour intensive for women activists and prospective candidates from diverse geographic and marginalised areas, after which a number expressed their intention to pursue candidacy."),
                ("Strengthening Young Leadership in Universities", "A 30-hour intensive covering democratic leadership, human rights, advocacy and campaigning, with noticeable improvement in academic performance, self-confidence and inter-university networking."),
                ("Overall impact", "More than 11,500 direct beneficiaries, 181 employment opportunities, and dozens of networking, coordination and awareness events strengthening cooperation with civil society, academic and community institutions."),
            ],
            me_title="Monitoring, evaluation and lessons learned",
            me=[
                ("Pre- and post-assessments", "Used to measure improvements in participants' knowledge and skills, particularly in vocational and rights-based training."),
                ("Field reports and meeting minutes", "Continuous documentation through trainers' reports, field coordinators' reports, meeting minutes and field visit records."),
                ("Focus group discussions", "Collecting participants' experiences, testimonies and success stories, particularly from displaced women and children in the camps."),
                ("Flexibility in crisis management", "Psychological first aid, emotional release and crisis management showed that psychosocial support and adaptability are essential to development work in unstable environments."),
                ("Linking skills with economic opportunity", "Women's economic empowerment is a pathway to social and rights-based empowerment; greater financial independence strengthens capacity to participate."),
            ],
            recs_title="Recommendations",
            recs=[
                ("Expand career guidance programmes", "Cover a wider range of fields and specialisations, with greater emphasis on practical training and hands-on learning."),
                ("Develop an online platform", "Facilitate communication among students, trainers and parents, and the exchange of information, materials and resources."),
                ("Increase cultural and arts activities", "Promote cultural awareness and strengthen recognition of the role of arts in community development."),
                ("Strengthen volunteer engagement", "Foster social responsibility while developing leadership, teamwork and civic engagement skills."),
                ("Targeted training for women with disabilities and unemployed youth", "With a particular focus on empowering marginalised and underserved groups."),
                ("Establish a permanent coordination mechanism", "Between civil society and government institutions, with annual forums for knowledge and experience sharing."),
                ("Build a unified digital beneficiary database", "To track beneficiaries' development pathways and support systematic measurement of longer-term outcomes."),
                ("Expand geographic coverage", "Extend the three projects into Area C, refugee camps and the most marginalised communities."),
                ("Establish an HDIP Alumni Network", "To sustain long-term networking and strengthen youth and women's networks nationally."),
            ],
        ),
        "ar": dict(
            year="2025", title="التقرير السنوي 2025",
            lead="التوجهات الاستراتيجية والمخرجات والنتائج والتوصيات لعام 2025.",
            summary_title="التوجهات الاستراتيجية",
            summary=[
                "تمحورت استراتيجيتنا خلال عام 2025 حول دفع عجلة التنمية المجتمعية، إذ وجّهنا ثقل جهودنا "
                "ومواردنا نحو استنهاض الطاقات الكامنة لدى الفئات الأكثر احتياجًا للدعم، وفي مقدمتها الشباب "
                "والمرأة. وجاءت هذه الأنشطة تجسيدًا لقناعتنا الراسخة بأن رفعة المجتمع الفلسطيني وازدهاره "
                "يرتبطان ارتباطًا وثيقًا بتمكين ركائزه الحيوية في أربعة محاور متقاطعة: الصحة، والتعليم، "
                "والتمكين، والاعتماد على الذات.",
            ],
            pillars_title="أربعة توجهات استراتيجية",
            pillars=[
                ("الرؤية التنموية والتمكين المجتمعي الشامل",
                 "تبنّى البرنامج التثقيف الصحي دعامة رئيسية للارتقاء بالصحة العامة وتحصين الوعي المجتمعي، "
                 "وأطلق حزمة من البرامج التوعوية عبر لقاءات تفاعلية وحلقات نقاشية في الصروح الأكاديمية "
                 "والمدرسية، إلى جانب حملات رقمية عبر وسائل التواصل الاجتماعي.",
                 ["تعزيز الصحة النفسية والصلابة المجتمعية.",
                  "رفع الوعي بالصحة الإنجابية وبناء الأسرة.",
                  "نشر ثقافة التغذية السليمة وأنماط الحياة الصحية.",
                  "تعزيز آليات الوقاية والحد من انتشار الأمراض المزمنة."]),
                ("التمكين الاقتصادي والتدريب المهني للمرأة",
                 "انطلاقًا من أن الاستقلال الاقتصادي للمرأة أساس لبناء مجتمعات صامدة، نفّذ البرنامج ورشًا "
                 "ودورات متخصصة في مجالات يتزايد الطلب عليها في السوق المحلي، تجاوزت المهارات التقنية إلى "
                 "إدارة المشاريع الصغيرة وريادة الأعمال والابتكار.",
                 ["التجميل والحلاقة — مهارات عملية لتأسيس مشاريع صغيرة أو للعمل.",
                  "التصوير والإنتاج الرقمي — مهارات المحتوى البصري وفرص العمل الحر.",
                  "أشغال الريزن والحرف اليدوية — الإبداع مقترنًا بتوليد الدخل."]),
                ("تعزيز البحث العلمي والبيئة الأكاديمية",
                 "اعتبر البرنامج البحث العلمي مسارًا لتعزيز العملية التعليمية، فقاد ندوات متخصصة ومحاضرات "
                 "توعوية وورش عمل تفاعلية.",
                 ["تشجيع الباحثين والأكاديميين الناشئين على اعتماد منهجيات بحثية سليمة.",
                  "تعزيز الوعي المجتمعي بالبحث العلمي كأداة لإنتاج المعرفة.",
                  "دعم التعلّم القائم على الأدلة ومعالجة التحديات الاستراتيجية."]),
                ("تكامل المعرفة عبر مشاريع الحق في التعليم",
                 "واصل البرنامج تنفيذ وإدارة مشروع الحق في التعليم بوصفه نموذجًا عمليًا لدمج التدخلات "
                 "التعليمية والتوعوية.",
                 ["معالجة الفجوات التعليمية الناجمة عن الظروف الاستثنائية والصعبة.",
                  "تعزيز التفكير النقدي وحل المشكلات والانخراط المجتمعي الإيجابي.",
                  "دمج مفاهيم الصحة العامة في التعليم غير الرسمي والأنشطة اللامنهجية."]),
            ],
            outputs_title="أبرز المخرجات والنتائج",
            outputs=[
                ("الأنشطة والبرامج الصحية", "73 دورة إسعاف أولي لـ1,460 طالبًا؛ 8 دورات في الصحة النفسية للمرأة لـ160 سيدة؛ 6 ورشات تثقيف صحي لـ420 طالبًا — بإجمالي نحو 2,040 مستفيدًا من الأنشطة الصحية الرئيسية."),
                ("نساء قادرات على تغيير المجتمع", "4 محافظات عبر 16 موقعًا محليًا؛ 100 مشارك في تدريب «حِرفة وفكرة»؛ 5 معارض بمشاركة 100 مستفيد؛ تشغيل 14 امرأة نازحة في مخيمين للأطفال استهدفا 380؛ 50 سيدة في التقييم والدعم النفسي ومخيم الصحة النفسية الشتوي؛ 12 لقاء تنسيق و10 لقاءات تحالف و4 موائد مستديرة وندوة ختامية لـ52 مشاركًا."),
                ("الحق في التعليم ومكوّناته", "100 جلسة توعوية رفعت الوعي بنسبة 80%؛ 3,300 طالب عبر 8 مراكز؛ 3,216 طالبًا في غزة عبر 67 صفًا تعويضيًا؛ 768 طالبًا في ورش البحث والتكنولوجيا والمهارات الحياتية؛ 200 طالب من 8 جامعات في حملة أخلاقيات البحث؛ 130 منحة دراسية؛ 170 طالبًا في ورش حقوقية؛ 1,100 طالب مدرسة في 34 صفًا تعويضيًا؛ 181 فرصة عمل."),
                ("نساء قياديات في المجالس المحلية", "تدريب مكثف من 30 ساعة لناشطات ومرشحات محتملات من مناطق جغرافية متنوعة ومهمّشة، عبّر بعدها عدد منهن عن نيتهن الترشح."),
                ("تعزيز القيادات الشابة في الجامعات", "تدريب مكثف من 30 ساعة في القيادة الديمقراطية وحقوق الإنسان والمناصرة والحملات، مع تحسّن ملحوظ في الأداء الأكاديمي والثقة بالنفس والتشبيك بين الجامعات."),
                ("الأثر الإجمالي", "أكثر من 11,500 مستفيد مباشر، و181 فرصة عمل، وعشرات فعاليات التشبيك والتنسيق والتوعية التي عزّزت التعاون مع مؤسسات المجتمع المدني والأكاديمية والمجتمعية."),
            ],
            me_title="المتابعة والتقييم والدروس المستفادة",
            me=[
                ("التقييم القبلي والبعدي", "لقياس التحسّن في معرفة المشاركين ومهاراتهم، خاصة في التدريب المهني والحقوقي."),
                ("التقارير الميدانية والمحاضر", "توثيق مستمر عبر تقارير المدربين ومنسقي الميدان ومحاضر الاجتماعات وسجلات الزيارات الميدانية."),
                ("مجموعات النقاش المركّزة", "لجمع تجارب المشاركين وشهاداتهم وقصص نجاحهم، خاصة من النساء النازحات والأطفال في المخيمات."),
                ("المرونة في إدارة الأزمات", "أظهرت أنشطة الإسعاف النفسي والتفريغ الانفعالي وإدارة الأزمات أن الدعم النفسي الاجتماعي والقدرة على التكيّف مكوّنان أساسيان للعمل التنموي في البيئات غير المستقرة."),
                ("ربط المهارة بالفرصة الاقتصادية", "التمكين الاقتصادي للمرأة مسار نحو التمكين الاجتماعي والحقوقي؛ فالاستقلال المالي يعزّز قدرتها على المشاركة."),
            ],
            recs_title="التوصيات",
            recs=[
                ("توسيع برامج التوجيه المهني", "لتشمل مجالات وتخصصات أوسع، مع تركيز أكبر على التدريب العملي والتعلّم التطبيقي."),
                ("تطوير منصة إلكترونية", "لتسهيل التواصل بين الطلبة والمدربين وأولياء الأمور وتبادل المعلومات والمواد والموارد."),
                ("زيادة الأنشطة الثقافية والفنية", "لتعزيز الوعي الثقافي وترسيخ الاعتراف بدور الفنون في التنمية المجتمعية."),
                ("تعزيز فرص العمل التطوعي", "لترسيخ روح المسؤولية الاجتماعية وتطوير مهارات القيادة والعمل الجماعي والانخراط المدني."),
                ("برامج تدريبية موجّهة للنساء ذوات الإعاقة والشباب العاطلين عن العمل", "مع تركيز خاص على تمكين الفئات المهمّشة والأقل حظًا."),
                ("إنشاء آلية تنسيق دائمة", "بين مؤسسات المجتمع المدني والمؤسسات الحكومية، مع منتديات سنوية لتبادل المعرفة والخبرات."),
                ("بناء قاعدة بيانات رقمية موحّدة للمستفيدين", "لتتبّع مساراتهم التنموية ودعم القياس المنهجي للنتائج والأثر على المدى الأطول."),
                ("توسيع التغطية الجغرافية", "لتشمل المشاريع الثلاثة مناطق «ج» والمخيمات والمجتمعات الأكثر تهميشًا."),
                ("إنشاء «شبكة خريجي البرنامج»", "للحفاظ على التشبيك طويل الأمد وتقوية شبكات الشباب والنساء على المستوى الوطني."),
            ],
        ),
    },

    "2023": {
        "en": dict(
            year="2023", title="Annual Report 2023",
            lead="Health, education and social and economic justice — the three areas HDIP focused on in 2023.",
            summary_title="Programme directions",
            summary=[
                "During 2023, HDIP focused on three main areas: health issues, education, and social, "
                "economic and development justice. These areas are particularly important because of their "
                "role in achieving genuine community development and building a society in which "
                "individuals' basic needs are met.",
                "HDIP placed particular emphasis on youth and women, recognising that these groups are "
                "among those most in need of support and assistance, and that reaching them extends the "
                "programme's services to the widest possible segment of society.",
            ],
            pillars_title="Health for All in 2023",
            pillars=[
                ("The right to health",
                 "The principle that underpins and is promoted throughout all HDIP programmes, as a "
                 "fundamental human right. Every individual should have access to the healthcare services "
                 "necessary to achieve and maintain good health.", []),
                ("Reducing health gaps",
                 "Raising awareness of \"Health for All\" to reduce disparities arising from economic, "
                 "social or geographical factors, ensuring services reach marginalised groups.", []),
                ("Prevention and awareness",
                 "Training that emphasises prevention and health education; when individuals receive "
                 "accurate information they become better able to make informed decisions.", []),
                ("Community participation",
                 "Encouraging local community organisations to participate in health-related "
                 "decision-making, strengthening programme effectiveness and health policy influence.", []),
                ("Improving quality of life",
                 "Ensuring access to healthcare to improve quality of life and life expectancy, through "
                 "inclusion, prevention and community participation.", []),
            ],
            outputs_title="Activities delivered",
            outputs=[
                ("Health awareness workshops", "222 workshops reaching approximately 2,000 participants across the West Bank and Gaza Strip, covering reproductive health, school health, personal hygiene, first aid, healthy nutrition, environmental health, psychological first aid and child health."),
                ("Training in health education skills", "200 participants trained to deliver workshops in their own communities, with particular emphasis on marginalised and remote areas far from service centres."),
                ("Awareness and advocacy campaigns", "Campaigns in marginalised areas advocating for the provision of healthcare and primary healthcare services."),
                ("Specific health trainings", "Reproductive health (Bethlehem); smoking cessation (Jenin); stress management (Ramallah); child health (Hebron, Jenin, Tulkarm); three environmental health courses; healthy habits for adults; emergency first aid across eight areas; crisis crowd management; psychological first aid (Jenin, Tulkarm); first aid for children in war situations."),
                ("Women Capable of Changing Society", "Implemented in Hebron, Jenin and Tulkarm, with 23 trainees per governorate across 20 villages or towns each. Training covered personal and life skills, social media marketing for handicrafts, income-generating small businesses, access to finance, local election awareness, personal financial planning, ICT and women's mental health."),
                ("Women Leaders in Local Councils", "62 training hours covering women's political empowerment, women's role in the electoral process, local election campaign management and effective participation, plus two exchange visits between project locations which produced a working paper on key strategies."),
                ("Youth Leadership Development in Universities", "62 hours of advanced capacity building covering social media, political parties, participation, campaigns, gender, advocacy and lobbying, non-violence, leadership, democracy, human rights and networking."),
                ("Student in Need Fund campaign", "An awareness campaign launched at seven local universities — Al-Quds Open, An-Najah National, Birzeit, Hebron, Al-Ahliya, Arab American and Al-Quds University–Abu Dis — using posters, brochures, workshops, discussion sessions and social media, with materials developed by the beneficiary students themselves."),
                ("Right to Education", "An electronic survey found 99% of participants considered education important; 31% because it helps them obtain suitable employment and 20% because it strengthens their leadership abilities. Awareness workshops, science and life-skills courses, and three career guidance meetings in Bethlehem, Nablus and Gaza followed."),
            ],
            recs_title="Overall totals",
            recs=[
                ("78 activities", "Total education and awareness activities implemented during 2023."),
                ("≈2,130 students", "Total beneficiaries — approximately 602 male and 1,528 female."),
                ("23 students with disabilities", "Included across the education and awareness activities."),
                ("222 workshops / ≈2,000 participants", "Health awareness workshops across the West Bank and Gaza Strip."),
            ],
            caveat="The 2023 source document carries a note from its translator stating that the Arabic "
                   "original contains number-formatting errors, and that the statistical tables should be "
                   "verified against the original before publication. The per-activity figures are indeed "
                   "internally inconsistent — the narrative and the statistical annex disagree (23 vs 35 "
                   "awareness sessions; 21 vs 43 school courses), and in two cases the male and female "
                   "sub-totals do not sum to the stated total. Only the overall totals above reconcile, so "
                   "only those are published here. The per-activity breakdown is withheld pending the "
                   "original document.",
        ),
        "ar": dict(
            year="2023", title="التقرير السنوي 2023",
            lead="الصحة والتعليم والعدالة الاجتماعية والاقتصادية — المجالات الثلاثة التي ركّز عليها البرنامج في 2023.",
            summary_title="توجهات البرنامج",
            summary=[
                "خلال عام 2023 ركّز البرنامج على ثلاثة مجالات رئيسية: القضايا الصحية، والتعليم، والعدالة "
                "الاجتماعية والاقتصادية والتنموية. وتكتسب هذه المجالات أهمية خاصة لدورها في تحقيق تنمية "
                "مجتمعية حقيقية وبناء مجتمع تُلبّى فيه الاحتياجات الأساسية للأفراد.",
                "وأولى البرنامج اهتمامًا خاصًا بالشباب والنساء، باعتبارهم من أكثر الفئات حاجة إلى الدعم "
                "والمساندة، وبما يتيح إيصال الخدمات إلى أوسع شريحة ممكنة من المجتمع.",
            ],
            pillars_title="الصحة للجميع في 2023",
            pillars=[
                ("الحق في الصحة", "المبدأ الذي تقوم عليه كل برامجنا بوصفه حقًا أساسيًا من حقوق الإنسان. ينبغي أن يحصل كل فرد على الخدمات الصحية اللازمة لبلوغ الصحة الجيدة والحفاظ عليها.", []),
                ("تقليص الفجوات الصحية", "التوعية بمفهوم «الصحة للجميع» للحد من التفاوتات الناتجة عن عوامل اقتصادية أو اجتماعية أو جغرافية، وضمان وصول الخدمات إلى الفئات المهمّشة.", []),
                ("الوقاية والتوعية", "تدريبات تركّز على الوقاية والتثقيف الصحي؛ فحين يحصل الأفراد على معلومات دقيقة يصبحون أقدر على اتخاذ قرارات مستنيرة.", []),
                ("المشاركة المجتمعية", "تشجيع المؤسسات المجتمعية على المشاركة في صنع القرار الصحي، بما يعزّز فعالية البرامج والتأثير في السياسات الصحية.", []),
                ("تحسين جودة الحياة", "ضمان الوصول إلى الرعاية الصحية لتحسين جودة الحياة ومتوسط العمر، عبر الشمول والوقاية والمشاركة المجتمعية.", []),
            ],
            outputs_title="الأنشطة المنفذة",
            outputs=[
                ("ورش التوعية الصحية", "222 ورشة استهدفت نحو 2,000 مشارك في الضفة الغربية وقطاع غزة، تناولت الصحة الإنجابية والصحة المدرسية والنظافة الشخصية والإسعافات الأولية والتغذية السليمة والصحة البيئية والإسعاف النفسي وصحة الطفل."),
                ("التدريب على مهارات التثقيف الصحي", "تدريب 200 مشارك على تنفيذ ورش في مجتمعاتهم، مع تركيز خاص على المناطق المهمّشة والنائية البعيدة عن مراكز الخدمات."),
                ("حملات التوعية والمناصرة", "حملات في المناطق المهمّشة للمناصرة من أجل توفير الرعاية الصحية وخدمات الرعاية الصحية الأولية."),
                ("تدريبات صحية متخصصة", "الصحة الإنجابية (بيت لحم)؛ الإقلاع عن التدخين (جنين)؛ إدارة الضغوط (رام الله)؛ صحة الطفل (الخليل وجنين وطولكرم)؛ ثلاث دورات في الصحة البيئية؛ العادات الصحية للبالغين؛ الإسعاف الأولي الطارئ في ثماني مناطق؛ إدارة الحشود في الأزمات؛ الإسعاف النفسي (جنين وطولكرم)؛ إسعاف الأطفال في حالات الحرب."),
                ("نساء قادرات على تغيير المجتمع", "نُفّذ في الخليل وجنين وطولكرم، بواقع 23 متدربة في كل محافظة و20 قرية أو بلدة لكل منها. غطّى التدريب المهارات الشخصية والحياتية والتسويق عبر وسائل التواصل للمنتجات اليدوية والمشاريع الصغيرة المدرّة للدخل والحصول على التمويل والتوعية بالانتخابات المحلية والتخطيط المالي الشخصي وتكنولوجيا المعلومات والصحة النفسية للمرأة."),
                ("نساء قياديات في المجالس المحلية", "62 ساعة تدريبية غطّت التمكين السياسي للمرأة ودورها في العملية الانتخابية وإدارة الحملات الانتخابية المحلية والمشاركة الفعّالة، إضافة إلى زيارتين تبادليتين بين مواقع المشروع أثمرتا ورقة عمل بأبرز الاستراتيجيات."),
                ("تطوير القيادات الشابة في الجامعات", "62 ساعة من بناء القدرات المتقدم شملت وسائل التواصل والأحزاب السياسية والمشاركة والحملات والنوع الاجتماعي والمناصرة وكسب التأييد واللاعنف والقيادة والديمقراطية وحقوق الإنسان والتشبيك."),
                ("حملة صندوق الطالب المحتاج", "حملة توعوية في سبع جامعات محلية — القدس المفتوحة والنجاح الوطنية وبيرزيت والخليل والأهلية والعربية الأمريكية وجامعة القدس–أبو ديس — باستخدام الملصقات والنشرات والورش وجلسات النقاش ووسائل التواصل، وقد شارك الطلبة المستفيدون أنفسهم في إعداد موادها."),
                ("الحق في التعليم", "أظهر استبيان إلكتروني أن 99% من المشاركين يعتبرون التعليم مهمًا؛ 31% لأنه يساعدهم في الحصول على عمل مناسب و20% لأنه يقوّي شخصيتهم القيادية. وتلت ذلك ورش توعية ودورات في العلوم والمهارات الحياتية وثلاثة لقاءات إرشاد مهني في بيت لحم ونابلس وغزة."),
            ],
            recs_title="المجاميع الكلية",
            recs=[
                ("78 نشاطًا", "إجمالي الأنشطة التعليمية والتوعوية المنفذة خلال 2023."),
                ("نحو 2,130 طالبًا", "إجمالي المستفيدين — نحو 602 من الذكور و1,528 من الإناث."),
                ("23 طالبًا من ذوي الإعاقة", "ضمن الأنشطة التعليمية والتوعوية."),
                ("222 ورشة / نحو 2,000 مشارك", "ورش التوعية الصحية في الضفة الغربية وقطاع غزة."),
            ],
            caveat="يحمل مستند عام 2023 ملاحظة من مترجمه تفيد بأن الأصل العربي يحتوي أخطاء في تنسيق الأرقام، "
                   "وأن الجداول الإحصائية ينبغي التحقق منها مقابل الأصل قبل النشر. والأرقام التفصيلية لكل "
                   "نشاط غير متسقة داخليًا بالفعل — إذ يختلف السرد عن الملحق الإحصائي (23 مقابل 35 جلسة "
                   "توعية؛ 21 مقابل 43 دورة مدرسية)، وفي حالتين لا يتطابق مجموع الذكور والإناث مع المجموع "
                   "المذكور. وتتسق المجاميع الكلية أعلاه وحدها، لذا نُشرت وحدها، مع حجب التفصيل بانتظار "
                   "المستند الأصلي.",
        ),
    },

    "2022": {
        "en": dict(
            year="2022", title="Annual Report 2022",
            lead="Health, education and social and economic justice, delivered largely through the community "
                 "knowledge libraries.",
            summary_title="Programme directions",
            summary=[
                "During 2022, HDIP focused its programmes on three main areas: health issues, education, and "
                "social and economic justice — areas considered essential to achieving genuine community "
                "development and building a society in which individuals' basic needs are met.",
                "HDIP placed particular emphasis on youth and women, considering them the groups most in "
                "need of support, advocacy, assistance and empowerment. Women account for more than 50% of "
                "the population, while youth of both genders represent approximately 75%, giving the "
                "institute an opportunity to reach the broadest possible segment of society.",
            ],
            pillars_title="Mechanism for implementing the objectives",
            pillars=[
                ("Publishing and conducting research and studies",
                 "Research, studies and scientific projects supporting statistical programmes and university "
                 "students' specialised projects.",
                 ["Preparing research projects and proposals on community topics.",
                  "Conducting studies and assisting in their publication and dissemination.",
                  "Training students, particularly persons with disabilities and women, in conducting research.",
                  "A comprehensive study on development needs in Area C."]),
                ("Adopting effective educational and health policies",
                 "Identifying priorities that require community attention and strengthening cooperation with "
                 "governmental and civil society organisations.",
                 ["Developing innovative models to follow up issues affecting youth and other groups.",
                  "Addressing health and education, media and social communication, poverty and unemployment.",
                  "Developing an integrated training programme supporting self-reliance in creating change."]),
                ("Raising awareness of education",
                 "Facilitating students' access to information and services, and organising training courses "
                 "across a wide range of subjects.",
                 ["First aid, health education, languages and calligraphy, personal development, computers.",
                  "Summer camps, the use of Braille, human resources, handicrafts, media, project management.",
                  "Books, references, periodicals, photocopying and printing, and computer laboratories.",
                  "Workshops on psychological support, health, leadership and access to employment."]),
                ("Working with marginalised areas",
                 "Workshops and campaigns in marginalised areas, coordinated with governmental bodies and "
                 "civil society organisations. As a continuation of the Right to Higher Education Campaign, "
                 "launched seven years earlier, awareness workshops were held for women, students and parents "
                 "through municipal councils in 11 locations.",
                 ["Joint activities with civil society organisations requiring field visits.",
                  "Courses on project development, literacy, working conditions and the role of women.",
                  "Raising awareness of the health environment in schools and marginalised communities.",
                  "Identifying the priorities and essential needs of marginalised communities."]),
            ],
            outputs_title="Community research and knowledge libraries",
            outputs=[
                ("Eight libraries, ~40,200 books", "Established with approximately 15,000 books, later updated and expanded to roughly 40,200 — cultural and scientific books, references, periodicals, university textbooks and encyclopaedias across scientific, cultural, social, political, literary and legal fields."),
                ("Eight librarians and ~80 volunteers", "A team of eight trained librarians supported by approximately 80 university student volunteers who classify and organise books, lend to users and coordinate training courses."),
                ("230 training courses, ~1,920 students", "Covering computer skills, first aid, scientific courses, languages, engineering, design and drawing, human resources, psychosocial support, scientific research, media and public relations, translation, life skills, music and remedial courses."),
                ("43 graduation projects", "University students supported in completing graduation projects, master's theses and scientific research studies."),
                ("Right to Higher Education workshops", "Run through the libraries on inclusion of persons with disabilities, educational policies in Palestine, the importance of scientific research, development of information systems, the status and quality of higher education, the role of civil society in educational policies, and freedom of movement and accessibility for persons with disabilities."),
            ],
            recs_title="Library facilities and services",
            recs=[
                ("Electronic research room", "Computers connected to the internet for educational and research use."),
                ("Training rooms", "Used for educational activities and the screening of documentary films."),
                ("Catalogued collection", "Systematically and electronically catalogued, with dedicated spaces for reading and research."),
                ("Lending, printing and courses", "Academic and cultural book lending, printing and photocopying, and specialised academic and skills-development courses. Priority is given to students from low-income families."),
            ],
        ),
        "ar": dict(
            year="2022", title="التقرير السنوي 2022",
            lead="الصحة والتعليم والعدالة الاجتماعية والاقتصادية، عبر مكتبات المعرفة المجتمعية بشكل أساسي.",
            summary_title="توجهات البرنامج",
            summary=[
                "خلال عام 2022 ركّز البرنامج على ثلاثة مجالات رئيسية: القضايا الصحية، والتعليم، والعدالة "
                "الاجتماعية والاقتصادية — وهي مجالات تُعدّ أساسية لتحقيق تنمية مجتمعية حقيقية وبناء مجتمع "
                "تُلبّى فيه الاحتياجات الأساسية للأفراد.",
                "وأولى البرنامج اهتمامًا خاصًا بالشباب والنساء بوصفهم الفئات الأكثر حاجة إلى الدعم والمناصرة "
                "والتمكين. فالنساء يشكّلن أكثر من 50% من السكان، بينما يمثّل الشباب من الجنسين نحو 75%، مما "
                "يتيح للمعهد الوصول إلى أوسع شريحة ممكنة من المجتمع.",
            ],
            pillars_title="آلية تنفيذ الأهداف",
            pillars=[
                ("نشر وإجراء البحوث والدراسات",
                 "بحوث ودراسات ومشاريع علمية تدعم البرامج الإحصائية ومشاريع طلبة الجامعات المتخصصة.",
                 ["إعداد مشاريع ومقترحات بحثية في قضايا مجتمعية متنوعة.",
                  "إجراء الدراسات والمساعدة في نشرها وتعميمها.",
                  "تدريب الطلبة، وخاصة ذوي الإعاقة والنساء، على إجراء البحث العلمي.",
                  "دراسة شاملة حول الاحتياجات التنموية في مناطق «ج»."]),
                ("اعتماد سياسات تعليمية وصحية فعّالة",
                 "تحديد الأولويات التي تحتاج اهتمامًا مجتمعيًا وتعزيز التعاون مع المؤسسات الحكومية والأهلية.",
                 ["تطوير نماذج مبتكرة لمتابعة القضايا التي تمس الشباب وفئات المجتمع الأخرى.",
                  "معالجة الصحة والتعليم والإعلام والتواصل الاجتماعي والفقر والبطالة.",
                  "تطوير برنامج تدريبي متكامل يدعم الاعتماد على الذات في إحداث التغيير."]),
                ("التوعية بأهمية التعليم",
                 "تسهيل وصول الطلبة إلى المعلومات والخدمات، وتنظيم دورات تدريبية في مجالات واسعة.",
                 ["الإسعاف الأولي والتثقيف الصحي واللغات والخط والتطوير الشخصي والحاسوب.",
                  "المخيمات الصيفية واستخدام طريقة برايل والموارد البشرية والحرف اليدوية والإعلام وإدارة المشاريع.",
                  "الكتب والمراجع والدوريات وخدمات التصوير والطباعة ومختبرات الحاسوب.",
                  "ورش في الدعم النفسي والصحة والقيادة وآليات الوصول إلى فرص العمل."]),
                ("العمل مع المناطق المهمّشة",
                 "ورش وحملات في المناطق المهمّشة بالتنسيق مع الجهات الحكومية ومؤسسات المجتمع المدني. "
                 "واستكمالًا لحملة الحق في التعليم العالي التي أُطلقت قبل سبع سنوات، نُفّذت ورش توعية للنساء "
                 "والطلبة وأولياء الأمور عبر المجالس البلدية في 11 موقعًا.",
                 ["أنشطة مشتركة مع مؤسسات المجتمع المدني تتطلب زيارات ميدانية.",
                  "دورات في تطوير المشاريع ومحو الأمية وتحسين ظروف العمل وتعزيز دور المرأة.",
                  "التوعية بأهمية تحسين البيئة الصحية في المدارس والمجتمعات المهمّشة.",
                  "تحديد أولويات وقضايا واحتياجات المجتمعات المهمّشة."]),
            ],
            outputs_title="مكتبات البحث والمعرفة المجتمعية",
            outputs=[
                ("ثماني مكتبات ونحو 40,200 كتاب", "أُنشئت بنحو 15,000 كتاب ثم جرى تحديثها وتوسيعها إلى نحو 40,200 — كتب ثقافية وعلمية ومراجع ودوريات وكتب جامعية وموسوعات علمية وثقافية واجتماعية وسياسية وأدبية وقانونية."),
                ("ثمانية أمناء مكتبات ونحو 80 متطوعًا", "فريق من ثمانية أمناء مدرَّبين يدعمهم نحو 80 متطوعًا من طلبة الجامعات يتولّون تصنيف الكتب وتنظيمها وإعارتها وتنسيق الدورات."),
                ("230 دورة تدريبية لنحو 1,920 طالبًا", "شملت مهارات الحاسوب والإسعاف الأولي والدورات العلمية واللغات والهندسة والتصميم والرسم والموارد البشرية والدعم النفسي والبحث العلمي والإعلام والعلاقات العامة والترجمة والمهارات الحياتية والموسيقى والدورات التعويضية."),
                ("43 مشروع تخرج", "دعم طلبة الجامعات في إنجاز مشاريع التخرج ورسائل الماجستير والدراسات البحثية."),
                ("ورش الحق في التعليم العالي", "نُفِّذت عبر المكتبات حول دمج ذوي الإعاقة والسياسات التعليمية في فلسطين وأهمية البحث العلمي وتطوير نظم المعلومات وواقع التعليم العالي وجودته ودور المجتمع المدني في السياسات التعليمية وحرية الحركة وإتاحة المؤسسات التعليمية لذوي الإعاقة."),
            ],
            recs_title="مرافق المكتبات وخدماتها",
            recs=[
                ("غرفة البحث الإلكتروني", "حواسيب متصلة بالإنترنت للاستخدام التعليمي والبحثي."),
                ("غرف التدريب", "تُستخدم للأنشطة التعليمية وعرض الأفلام الوثائقية."),
                ("مقتنيات مفهرسة", "مفهرسة منهجيًا وإلكترونيًا، مع مساحات مخصصة للقراءة والبحث."),
                ("الإعارة والطباعة والدورات", "إعارة الكتب الأكاديمية والثقافية والطباعة والتصوير ودورات أكاديمية ومهارية متخصصة، مع إعطاء الأولوية لطلبة الأسر محدودة الدخل."),
            ],
        ),
    },
}

# --------------------------------------------------------------------------
# 2025 news articles, from the approved "suggested first articles" list
# --------------------------------------------------------------------------
NEWS_2025 = [
    dict(slug="research-ethics-campaign", photo="youth-training", area="research",
         project="right-to-education", date="2025",
         en=dict(title="Research Ethics Campaign reaches 200 students across 8 universities",
                 tag="Research", date="2025",
                 summary="A campaign on academic integrity, with a simplified guide to preparing scientific "
                         "research distributed as a lasting reference.",
                 body=["The Scientific Research Ethics Campaign reached 8 local universities and engaged 200 "
                       "students (120 female, 80 male).",
                       "As part of the campaign, a simplified guide to scientific research preparation was "
                       "distributed, giving students a sustainable reference tool to promote academic "
                       "integrity and improve the quality of graduation and research projects.",
                       "An accompanying awareness campaign against plagiarism ran across several "
                       "universities, with practical workshops in Hebron, Bethlehem, Nablus and Ramallah.",
                       "Alongside the campaign, 768 students (460 female, 308 male) took part in workshops "
                       "on scientific research, technology and life skills, delivered across 144 training "
                       "hours covering hypothesis formulation and results analysis, artificial intelligence, "
                       "cybersecurity and programming, and communication, time management, critical thinking "
                       "and teamwork."]),
         ar=dict(title="حملة أخلاقيات البحث العلمي تصل إلى 200 طالب في 8 جامعات",
                 tag="البحث", date="2025",
                 summary="حملة حول النزاهة الأكاديمية، وُزّع خلالها دليل مبسّط لإعداد البحث العلمي كمرجع دائم.",
                 body=["وصلت حملة أخلاقيات البحث العلمي إلى 8 جامعات محلية وشارك فيها 200 طالب وطالبة "
                       "(120 من الإناث و80 من الذكور).",
                       "وضمن الحملة وُزّع دليل مبسّط لإعداد البحث العلمي، يوفّر للطلبة أداة مرجعية مستدامة "
                       "لتعزيز النزاهة الأكاديمية وتحسين جودة مشاريع التخرج والبحوث.",
                       "ورافقت ذلك حملة توعوية لمكافحة الانتحال العلمي في عدة جامعات، تخللتها ورش عملية في "
                       "الخليل وبيت لحم ونابلس ورام الله.",
                       "وإلى جانب الحملة، شارك 768 طالبًا (460 من الإناث و308 من الذكور) في ورش حول البحث "
                       "العلمي والتكنولوجيا والمهارات الحياتية، نُفّذت عبر 144 ساعة تدريبية شملت صياغة "
                       "الفرضيات وتحليل النتائج والذكاء الاصطناعي والأمن السيبراني والبرمجة والتواصل وإدارة "
                       "الوقت والتفكير النقدي والعمل الجماعي."])),

    dict(slug="camps-displaced-women", photo="women-able-group", area="women",
         project="women-able", date="2025",
         en=dict(title="Fourteen displaced women run summer and winter camps for 380 children",
                 tag="Women's Empowerment", date="2025",
                 summary="A response to displacement in Jenin and Tulkarm that paid displaced women to run "
                         "children's camps — income for them, a safe space for the children.",
                 body=["In response to the displacement affecting communities in Jenin and Tulkarm, the "
                       "Women Able to Change Society project placed particular emphasis on creating "
                       "employment to support displaced women and strengthen their resilience.",
                       "Fourteen displaced women were employed in a children's summer camp that reached 160 "
                       "participants. The experience was then replicated through a winter camp reaching 220.",
                       "Together the two camps gave children a safe environment for artistic, recreational "
                       "and group activities. At the same time, the employment gave displaced women income, "
                       "strengthened their self-confidence and enabled them to develop new leadership and "
                       "facilitation skills. Both interventions contributed to social cohesion and community "
                       "solidarity in the targeted communities.",
                       "A three-day evaluation and psychosocial support workshop of 25 sessions, and a "
                       "separate three-day winter mental health camp, together benefited 50 women, using "
                       "mindfulness, reflective writing and drawing to help participants express emotion and "
                       "manage the pressures of the prevailing circumstances."]),
         ar=dict(title="أربع عشرة امرأة نازحة يدرن مخيمين صيفي وشتوي لـ380 طفلًا",
                 tag="تمكين المرأة", date="2025",
                 summary="استجابة لواقع النزوح في جنين وطولكرم، وفّر المشروع عملًا مأجورًا لنساء نازحات "
                         "لإدارة مخيمات الأطفال — دخل لهن ومساحة آمنة للأطفال.",
                 body=["استجابةً لواقع النزوح الذي يؤثر على المجتمعات في جنين وطولكرم، أولى مشروع نساء قادرات "
                       "على تغيير المجتمع اهتمامًا خاصًا بإيجاد فرص عمل لدعم النساء النازحات وتعزيز صمودهن.",
                       "جرى تشغيل أربع عشرة امرأة نازحة في مخيم صيفي للأطفال استهدف 160 مشاركًا، ثم تكرّرت "
                       "التجربة في مخيم شتوي استهدف 220.",
                       "ووفّر المخيمان للأطفال بيئة آمنة لأنشطة فنية وترفيهية وجماعية، فيما وفّر التشغيل "
                       "للنساء النازحات دخلًا وعزّز ثقتهن بأنفسهن ومكّنهن من تطوير مهارات جديدة في القيادة "
                       "والتيسير. وأسهم التدخلان في تعزيز التماسك الاجتماعي والتضامن المجتمعي.",
                       "كما استفادت 50 سيدة من ورشة تقييم ودعم نفسي اجتماعي على مدار ثلاثة أيام شملت 25 "
                       "جلسة، ومن مخيم شتوي متخصص في الصحة النفسية لثلاثة أيام، استُخدمت فيهما اليقظة "
                       "الذهنية والكتابة التأملية والرسم لمساعدة المشاركات على التعبير عن مشاعرهن وإدارة "
                       "ضغوط الظروف القائمة."])),

    dict(slug="scholarships-2025", photo="conference-hall", area="education",
         project="right-to-education", date="2025",
         en=dict(title="130 scholarships and 181 jobs: the Right to Education Support Project 2",
                 tag="Education", date="2025",
                 summary="Scholarships covering tuition for 130 students, an intensive remedial programme "
                         "for 1,100 school students, and 181 employment opportunities created.",
                 body=["Throughout 2025 the Right to Education Support Project 2 responded to the financial "
                       "and academic barriers facing Palestinian students through four complementary areas: "
                       "scholarships for low-income students, critical thinking and research skills, "
                       "rights-based advocacy, and remedial teaching for school students.",
                       "Implementation rates for most targeted results ranged between 95% and 100%.",
                       "Scholarship coordinators were contracted, an updated selection protocol adopted and "
                       "an electronic application form introduced to make screening fair and efficient. HDIP "
                       "coordinated with four partner Palestinian universities, including Birzeit University "
                       "and the Arab American University, to nominate eligible students. Scholarships "
                       "covering tuition fees and educational costs went to 130 students — 96 female and 34 "
                       "male.",
                       "An intensive remedial education programme was established across the North, Central "
                       "and South regions, with 34 classes for students experiencing learning difficulties. "
                       "1,100 school students benefited from 3,129 actual teaching hours across Arabic, "
                       "English, mathematics, science and life skills. Pre- and post-assessments showed "
                       "noticeable improvement in academic performance and self-confidence.",
                       "Across its components the project created 181 permanent and temporary employment "
                       "opportunities for qualified educational and administrative personnel."]),
         ar=dict(title="130 منحة دراسية و181 فرصة عمل: مشروع دعم الحق في التعليم 2",
                 tag="التعليم", date="2025",
                 summary="منح تغطي الرسوم لـ130 طالبًا، وبرنامج تعويضي مكثف لـ1,100 طالب مدرسة، و181 فرصة عمل.",
                 body=["خلال عام 2025 استجاب مشروع دعم الحق في التعليم 2 للعوائق المالية والأكاديمية التي "
                       "تواجه الطلبة الفلسطينيين عبر أربعة مجالات متكاملة: المنح الدراسية للطلبة محدودي "
                       "الدخل، وتنمية التفكير النقدي ومهارات البحث، والمناصرة الحقوقية، والتعليم التعويضي "
                       "لطلبة المدارس.",
                       "وتراوحت نسب التنفيذ لمعظم النتائج المستهدفة بين 95% و100%.",
                       "جرى التعاقد مع منسقي منح، واعتُمد بروتوكول اختيار محدّث ونموذج تقديم إلكتروني لجعل "
                       "الفرز عادلًا وفعّالًا. ونسّق البرنامج مع أربع جامعات فلسطينية شريكة، منها جامعة "
                       "بيرزيت والجامعة العربية الأمريكية، لترشيح الطلبة المؤهلين. وذهبت المنح التي تغطي "
                       "الرسوم والتكاليف التعليمية إلى 130 طالبًا — 96 من الإناث و34 من الذكور.",
                       "وأُنشئ برنامج تعليم تعويضي مكثف في المناطق الشمالية والوسطى والجنوبية، شمل 34 صفًا "
                       "للطلبة الذين يواجهون صعوبات تعلّمية. واستفاد 1,100 طالب مدرسة من 3,129 ساعة تدريس "
                       "فعلية في اللغة العربية والإنجليزية والرياضيات والعلوم والمهارات الحياتية. وأظهرت "
                       "التقييمات القبلية والبعدية تحسنًا ملحوظًا في الأداء الأكاديمي والثقة بالنفس.",
                       "وعبر مكوّناته أوجد المشروع 181 فرصة عمل دائمة ومؤقتة للكوادر التعليمية والإدارية "
                       "المؤهلة."])),
]

# Gaps that remain after the 2022/2023/2025 batches arrived
GAPS_REMAINING = {
    "en": [
        ("Team & Board", "Names, roles and photographs still not supplied."),
        ("Donors and partners", "No list or logos supplied. Only Friedrich-Ebert-Stiftung and Olof Palme International Center are identifiable, from banners in the 2024 photographs."),
        ("Annual report PDFs", "No PDFs supplied, so report pages have no download."),
        ("Contact details", "Address, phone, email and social links still need confirmation."),
        ("2023 statistical annex", "The per-activity figures are internally inconsistent and the document itself asks for them to be verified against the original. Only the reconciling totals are published."),
        ("Women Able 2024 — English text", "The English half of the 2024 file contains Right to Education text; the English 2024 phase is translated from the Arabic."),
        ("Photography for 2022, 2023 and 2025", "Programme photographs were supplied only with the 2024 batch."),
        ("Project donors per phase", "Which donor funded which project in which year is not recorded in any document."),
        ("Online donations", "No decision recorded on whether the site should accept donations."),
    ],
    "ar": [
        ("الفريق ومجلس الإدارة", "لم تُزوَّد الأسماء والمهام والصور بعد."),
        ("الممولون والشركاء", "لم تُزوَّد قائمة أو شعارات. ولا يمكن تمييز سوى مؤسسة فريدريش إيبرت ومركز أولوف بالمه الدولي من لافتات في صور 2024."),
        ("ملفات التقارير السنوية PDF", "لم تُزوَّد، لذلك لا يوجد تنزيل في صفحات التقارير."),
        ("بيانات الاتصال", "العنوان والهاتف والبريد وروابط التواصل بحاجة إلى تأكيد."),
        ("الملحق الإحصائي 2023", "الأرقام التفصيلية غير متسقة داخليًا، والمستند نفسه يطلب التحقق منها مقابل الأصل. ولم يُنشر سوى المجاميع المتسقة."),
        ("نساء قادرات 2024 — النص الإنجليزي", "القسم الإنجليزي في ملف 2024 يحتوي نص الحق في التعليم؛ ومرحلة 2024 الإنجليزية مترجمة عن العربية."),
        ("صور أعوام 2022 و2023 و2025", "لم تُزوَّد صور برامجية إلا مع دفعة عام 2024."),
        ("ممولو كل مرحلة من المشاريع", "لا يسجّل أي مستند أي ممول موّل أي مشروع في أي عام."),
        ("التبرعات الإلكترونية", "لا يوجد قرار مسجّل بشأن قبول الموقع للتبرعات."),
    ],
}

# --------------------------------------------------------------------------
# Contextual photography (Wikimedia Commons) — alt text and bilingual captions.
# These are NOT HDIP's own work; captions name place and subject only.
# --------------------------------------------------------------------------
CONTEXT_PHOTOS = {
    "ramallah-city": dict(
        alt="Residential blocks spreading across the hills of Ramallah under a clear sky",
        en="Ramallah, September 2024", ar="رام الله، أيلول 2024"),
    "al-bireh": dict(
        alt="The city of Al-Bireh seen across open ground from behind a wire fence",
        en="Al-Bireh, Ramallah governorate", ar="البيرة، محافظة رام الله"),
    "ramallah-oldcity": dict(
        alt="Wide view over the old city of Ramallah",
        en="Ramallah old city", ar="البلدة القديمة، رام الله"),
    "ramallah-market": dict(
        alt="A man walking past a taxi in the busy central market district of Ramallah",
        en="Central market, Ramallah", ar="السوق المركزي، رام الله"),
    "ramallah-hills": dict(
        alt="A concrete watchtower and barrier wall section on the edge of Ramallah, with a village on the far hillside",
        en="Barrier and watchtower, Ramallah district", ar="الجدار وبرج مراقبة، محافظة رام الله"),
    "checkpoint": dict(
        alt="A road checkpoint with a watchtower beside a signpost reading Ramallah in Hebrew, Arabic and English",
        en="Checkpoint on the road to Ramallah", ar="حاجز على الطريق إلى رام الله"),
    "hospital-turmusayya": dict(
        alt="The curved glass frontage of Hugo Chávez Hospital at dusk",
        en="Hugo Chávez Hospital, Turmus Ayya", ar="مستشفى هوغو تشافيز، ترمسعيا"),
    "westbank-satellite": dict(
        alt="Satellite photograph of the West Bank showing built-up areas threaded through brown hills",
        en="The West Bank from the ISS, Expedition 75", ar="الضفة الغربية من محطة الفضاء الدولية، البعثة 75"),
    "closures-map": dict(
        alt="United Nations map of Ramallah governorate marking checkpoints, roadblocks, earthmounds and the route of the barrier",
        en="Ramallah closures — UN OCHA Humanitarian Atlas, December 2011",
        ar="إغلاقات رام الله — الأطلس الإنساني، مكتب الأمم المتحدة لتنسيق الشؤون الإنسانية، كانون الأول 2011"),
    "women-workplace": dict(
        alt="Two women walking up a narrow stone-walled street, the town spread over the hill behind them",
        en="A village street, Palestine", ar="شارع في قرية فلسطينية"),
    "olives-nablus": dict(
        alt="An older man reaching into an olive tree during the harvest while a boy holds the bucket",
        en="Olive harvest near Nablus", ar="موسم قطف الزيتون قرب نابلس"),
    "olive-planting": dict(
        alt="A farmer kneeling on terraced ground, setting an olive sapling into the soil",
        en="Planting olive trees, Beit Ommar, 2010", ar="زراعة أشجار الزيتون، بيت أمر، 2010"),
}

# One photograph per page hero — no image heads more than one surface.
HERO_PHOTOS = {
    "about":                   "al-bireh",
    "work":                    "westbank-satellite",
    "area-health":             "hospital-turmusayya",
    "area-education":          "ramallah-oldcity",
    "area-women":              "women-able-group",
    "area-youth":              "youth-training",
    "area-research":           "closures-map",
    "projects":                "women-able-session",
    "project-right-to-education": "checkpoint",
    "project-women-able":      "conference-closing",
    "project-women-leaders":   "women-leaders-training",
    "project-youth-leadership": "ramallah-market",
    "reports":                 "ramallah-oldcity",
    "report-2022":             "olives-nablus",
    "report-2023":             "olive-planting",
    "report-2024":             "women-workplace",
    "report-2025":             "women-leaders-training",
    "news":                    "conference-hall",
    "contact":                 "ramallah-hills",
    "credits":                 "ramallah-city",
}

# --------------------------------------------------------------------------
# Page endings — every surface gets a close, not a drop into the footer
# --------------------------------------------------------------------------
ENDINGS = {
    "en": dict(
        project=("Work with this project", "HDIP partners with donors, councils and community organisations on delivery, training and evaluation.", "Contact us"),
        area=("Partner with us on this work", "HDIP works with local and international partners on research, training, evaluation and community programmes.", "Contact us"),
        report=("Read another year", "Annual reporting from 2022 onward sets each year's directions, activities and recommendations side by side.", "All reports"),
        about=("Work with HDIP", "We welcome partners on research, training, evaluation and community programmes.", "Contact us"),
        news=("More from the programme", "Conference statements, campaign launches and findings from HDIP's units.", "All news"),
    ),
    "ar": dict(
        project=("اعمل معنا في هذا المشروع", "يعمل البرنامج مع الممولين والمجالس والمؤسسات المجتمعية في التنفيذ والتدريب والتقييم.", "اتصل بنا"),
        area=("كن شريكًا في هذا العمل", "يعمل البرنامج مع شركاء محليين ودوليين في البحث والتدريب والتقييم والبرامج المجتمعية.", "اتصل بنا"),
        report=("اقرأ عامًا آخر", "التقارير السنوية منذ 2022 تضع توجهات كل عام وأنشطته وتوصياته جنبًا إلى جنب.", "كل التقارير"),
        about=("اعمل مع البرنامج", "نرحّب بالشركاء في البحث والتدريب والتقييم والبرامج المجتمعية.", "اتصل بنا"),
        news=("المزيد من البرنامج", "بيانات المؤتمرات وإطلاق الحملات ونتائج وحدات البرنامج.", "كل الأخبار"),
    ),
}

# The closures map is the one object on the site that is unmistakably about
# this place. It ships untinted (.media--true) beside the access argument.
CLOSURES_NOTE = {
    "en": dict(
        title="A school you cannot reach",
        body="The Right to Education Project runs across eight governorates including Gaza. What that costs is "
             "visible in documents like this one: the December 2011 humanitarian atlas recorded 104 closures in "
             "the Ramallah governorate alone — checkpoints, partial checkpoints, earthmounds, roadblocks, road "
             "gates, trenches and earth walls. Closure is why the project is delivered through local centres "
             "rather than from one place, and why 2024 ran on an emergency-adapted plan."),
    "ar": dict(
        title="مدرسة لا يمكنك الوصول إليها",
        body="يُنفَّذ مشروع الحق في التعليم في ثماني محافظات بما فيها غزة. وتظهر كلفة ذلك في وثائق كهذه: سجّل "
             "الأطلس الإنساني في كانون الأول 2011 مئة وأربعة إغلاقات في محافظة رام الله وحدها — حواجز وحواجز "
             "جزئية وسواتر ترابية ومكعبات إسمنتية وبوابات وخنادق وجدران ترابية. الإغلاق هو سبب تنفيذ المشروع "
             "عبر مراكز محلية لا من مكان واحد، وسبب اعتماد خطة طوارئ في عام 2024."),
}

# --------------------------------------------------------------------------
# Hero slideshow — HDIP's own programme photography
# --------------------------------------------------------------------------
# A full-bleed hero needs genuine resolution. HDIP's own programme photographs
# came out of Word documents and top out at 813-2048px, so only youth-training
# is large enough; the rest of the stage uses the high-resolution Palestine
# photography, which is captioned and credited as contextual on every slide.
# If HDIP supplies the original camera files, put their photographs back here.
HERO_SLIDES = ["ramallah-city", "youth-training", "olives-nablus",
               "hospital-turmusayya", "checkpoint", "women-workplace"]

SLIDESHOW_UI = {
    "en": dict(label="HDIP programme photography", pause="Pause the slideshow",
               play="Play the slideshow", choose="Choose a photograph",
               slide="Photograph {n} of {total}",
               prev="Previous photograph", next="Next photograph"),
    "ar": dict(label="صور برامج البرنامج", pause="إيقاف العرض",
               play="تشغيل العرض", choose="اختر صورة",
               slide="الصورة {n} من {total}",
               prev="الصورة السابقة", next="الصورة التالية"),
}
