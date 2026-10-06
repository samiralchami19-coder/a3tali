import json, re, collections, sys
d = {k: v for k, v in json.load(open("dtc.json", encoding="utf-8")).items() if v and "Reserved" not in v}
FIX = {"lntake":"Intake","OBDResponse":"Response","Circuit/ Open":"Circuit/Open","Circuit /Open":"Circuit/Open","  ":" "}
MW = [  # multi-word units, longest first
("Exhaust Gas Recirculation","إعادة تدوير غاز العادم EGR"),("Secondary Air Injection System","نظام حقن الهواء الثانوي"),("Secondary Air Injection","حقن الهواء الثانوي"),
("Evaporative Emission System","نظام انبعاثات البخر EVAP"),("Evaporative Emission","انبعاثات البخر EVAP"),("Turbo/Super Charger","التيربو أو السوبرتشارجر"),("Turbocharger","التيربو"),
("Intake Manifold Runner","مجاري مشعب السحب"),("Intake Manifold Tuning Valve","صمام ضبط مشعب السحب"),("Intake Manifold","مشعب السحب"),("Manifold Absolute Pressure","الضغط المطلق للمشعب MAP"),("Barometric Pressure","الضغط الجوي"),
("Mass or Volume Air Flow","تدفق الهواء MAF"),("Mass Air Flow","تدفق الهواء MAF"),("Intake Air Temperature","حرارة هواء السحب"),("Engine Coolant Temperature","حرارة سائل تبريد المحرك"),("Engine Oil Temperature","حرارة زيت المحرك"),("Engine Oil Pressure","ضغط زيت المحرك"),
("Throttle/Pedal Position Sensor/Switch","حساس أو مفتاح موضع الخانق/الدواسة"),("Throttle Position","موضع الخانق"),("Throttle Actuator Control","التحكم في مشغّل الخانق"),("Throttle Actuator","مشغّل الخانق"),("Accelerator Pedal Position","موضع دواسة الوقود"),
("Camshaft Position Actuator","مشغّل توقيت عمود الكامات"),("Camshaft Position","موضع عمود الكامات"),("Crankshaft Position","موضع عمود الكرنك"),("Ignition Coil","كويل الإشعال"),("Fuel Injector","بخاخ الوقود"),("Fuel Pump","مضخة الوقود"),("Fuel Rail","سكة الوقود"),("Fuel Level","مستوى الوقود"),
("Fuel Trim","تعديل نسبة الوقود"),("Fuel Composition","تركيب الوقود"),("Fuel Temperature","حرارة الوقود"),("Fuel Pressure","ضغط الوقود"),("Fuel Shutoff Valve","صمام قطع الوقود"),("Fuel Volume Regulator","منظّم كمية الوقود"),("Injection Pump","مضخة الحقن"),("Injection Timing","توقيت الحقن"),
("O2 Sensor","حساس الأكسجين"),("HO2S Heater","سخان حساس الأكسجين"),("HO2S","حساس الأكسجين المسخَّن"),("NOx Sensor","حساس NOx"),("Knock Sensor","حساس الطرق"),("Vehicle Speed Sensor","حساس سرعة المركبة"),("Wheel Speed Sensor","حساس سرعة العجلة"),
("Catalyst System Efficiency Below Threshold","كفاءة الدبة (المحوّل الحفاز) أقل من الحد"),("Catalyst Temperature","حرارة الدبة (المحوّل الحفاز)"),("Catalyst","الدبة (المحوّل الحفاز)"),("Particulate Trap","فلتر الجسيمات"),("Particulate Filter","فلتر الجسيمات"),
("Glow Plug/Heater","شمعة التوهج/السخان"),("Glow Plug","شمعة التوهج"),("Shift Solenoid","سولينويد النقل"),("Pressure Control Solenoid","سولينويد التحكم بالضغط"),("Torque Converter Clutch","كلتش محوّل العزم"),("Torque Converter","محوّل العزم"),
("Transmission Fluid Pressure","ضغط زيت ناقل الحركة"),("Transmission Fluid Temperature","حرارة زيت ناقل الحركة"),("Transmission Fluid","زيت ناقل الحركة"),("Transmission Control System","نظام التحكم بناقل الحركة"),("Transmission Control Module","وحدة التحكم بناقل الحركة TCM"),("Transmission Range","وضع ناقل الحركة"),
("Input/Turbine Speed","سرعة عمود الدخل/التوربين"),("Output Speed","سرعة عمود الخرج"),("Intermediate Shaft Speed","سرعة العمود الأوسط"),("Output Shaft Speed","سرعة عمود الخرج"),("Gear Ratio","نسبة الغيار"),("Transfer Case","علبة التوزيع"),
("Rocker Arm Actuator","مشغّل ذراع الصمام"),("Cylinder Deactivation","إيقاف الأسطوانات"),("Intake Valve Control Solenoid","سولينويد التحكم بصمام السحب"),("Exhaust Valve Control Solenoid","سولينويد التحكم بصمام العادم"),
("Exhaust Gas Temperature","حرارة غاز العادم"),("Exhaust Pressure","ضغط العادم"),("Reductant Injector","بخاخ سائل الاختزال (اليوريا)"),("Reductant","سائل الاختزال (اليوريا)"),("A/C Refrigerant Pressure","ضغط فريون المكيف"),("A/C Clutch Relay","ريليه كلتش المكيف"),("A/C","المكيف"),
("Cruise Control Multi-Function Input","دخل مثبت السرعة متعدد الوظائف"),("Cruise Control","مثبت السرعة"),("Brake Switch","مفتاح الفرامل"),("Brake Booster","معزّز الفرامل"),("Power Steering Pressure","ضغط مساعد المقود"),("Power Steering","مساعد المقود"),
("Sensor Reference Voltage","الجهد المرجعي للحساسات"),("Reference Voltage","الجهد المرجعي"),("System Voltage","جهد النظام"),("Supply Voltage","جهد التغذية"),("Battery Voltage","جهد البطارية"),
("High Speed CAN Communication Bus","ناقل CAN عالي السرعة"),("Medium Speed CAN Communication Bus","ناقل CAN متوسط السرعة"),("Low Speed CAN Communication Bus","ناقل CAN منخفض السرعة"),("Vehicle Communication Bus","ناقل اتصال المركبة"),("CAN Communication Bus","ناقل CAN"),
("Control Module","وحدة التحكم"),("ECM/PCM","كمبيوتر المحرك ECM/PCM"),("PCM/ECM/TCM","كمبيوتر المحرك أو ناقل الحركة"),("Body Control Module","وحدة التحكم بالهيكل BCM"),("Instrument Panel Cluster","لوحة العدادات"),("Anti-Lock Brake System","نظام ABS"),
("Restraints Control Module","وحدة الوسائد الهوائية"),("Steering Angle Sensor","حساس زاوية المقود"),("Yaw Rate Sensor","حساس معدل الانحراف"),("Engine Speed","سرعة دوران المحرك"),("Idle Air Control","التحكم بهواء السلانسيه"),("Idle Control System","نظام التحكم بالسلانسيه"),("Idle","السلانسيه"),
("Intake Air Heater","سخان هواء السحب"),("Cooling Fan","مروحة التبريد"),("Fan","المروحة"),("Thermostat","الثرموستات"),("Generator","الدينمو"),("Starter Relay","ريليه السلف"),("Starter","السلف"),("Immobilizer","مانع التشغيل"),
("Wastegate Solenoid","سولينويد بوابة التيربو"),("Wastegate","بوابة التيربو"),("Boost Sensor","حساس ضغط التيربو"),("Boost","ضغط التيربو"),("Purge Control Valve","صمام التنفيس"),("Purge","التنفيس"),("Vent Valve","صمام التهوية"),("Vent","التهوية"),("Leak Detection Pump","مضخة كشف التسريب"),
("Variable Valve Timing","توقيت الصمامات المتغير"),("Valve Timing","توقيت الصمامات"),("Malfunction Indicator Lamp","لمبة Check Engine"),("MIL","لمبة Check Engine"),("Park/Neutral","P/N"),
]
W = {"sensor":"حساس","sensor/switch":"حساس/مفتاح","switch":"مفتاح","solenoid":"سولينويد","valve":"صمام","valve/solenoid":"صمام/سولينويد","relay":"ريليه","motor":"محرك كهربائي","pump":"مضخة","module":"وحدة","actuator":"مشغّل","heater":"سخان","injector":"بخاخ",
"coil":"كويل","system":"نظام","control":"التحكم","engine":"المحرك","transmission":"ناقل الحركة","fuel":"الوقود","air":"الهواء","oil":"الزيت","coolant":"سائل التبريد","exhaust":"العادم","intake":"السحب","gas":"غاز","pressure":"ضغط","temperature":"حرارة",
"position":"موضع","speed":"سرعة","voltage":"جهد","current":"تيار","signal":"إشارة","input":"دخل","output":"خرج","power":"القدرة","supply":"تغذية","ground":"الأرضي","level":"مستوى","flow":"تدفق","timing":"توقيت","torque":"العزم","clutch":"الكلتش","gear":"الغيار",
"shift":"النقل","brake":"الفرامل","throttle":"الخانق","pedal":"الدواسة","throttle/pedal":"الخانق/الدواسة","cylinder":"الأسطوانة","ignition":"الإشعال","injection":"الحقن","primary":"الابتدائي","secondary":"الثانوي","primary/secondary":"الابتدائي/الثانوي",
"manifold":"المشعب","camshaft":"عمود الكامات","crankshaft":"عمود الكرنك","knock":"الطرق","misfire":"تفويت","vehicle":"المركبة","battery":"البطارية","charging":"الشحن","charge":"الشحن","steering":"المقود","door":"الباب","lamp":"لمبة","fan":"المروحة",
"regulator":"منظّم","converter":"المحوّل","hydraulic":"الهيدروليكي","evap":"EVAP","emission":"الانبعاثات","emissions":"الانبعاثات","recirculation":"إعادة التدوير","bypass":"تحويلة","vacuum":"الخلخلة","leak":"تسريب","leakage":"تسريب","purge":"التنفيس","vent":"التهوية",
"reference":"المرجع","sense":"استشعار","feedback":"التغذية الراجعة","request":"طلب","data":"بيانات","software":"البرنامج","memory":"الذاكرة","processor":"المعالج","programming":"البرمجة","internal":"داخلي","performance":"أداء","efficiency":"كفاءة","ratio":"نسبة",
"bus":"ناقل","communication":"اتصال","link":"رابط","serial":"تسلسلي","gateway":"البوابة","unit":"وحدة","group":"مجموعة","bank":"الصف","side":"جهة","front":"الأمامي","rear":"الخلفي","left":"الأيسر","right":"الأيمن","center":"الأوسط","upper":"العلوي","lower":"السفلي",
"reverse":"الرجوع","forward":"الأمامي","drive":"القيادة","park":"الوقوف","neutral":"الحياد","manual":"اليدوي","auto":"التلقائي","automatic":"التلقائي","mode":"وضع","select":"اختيار","lever":"ذراع","range":"مدى","lock":"قفل","lockup":"القفل","apply":"التعشيق",
"shaft":"عمود","intermediate":"الأوسط","wheel":"العجلة","turbine":"التوربين","runner":"المجاري","tuning":"الضبط","rocker":"ذراع الصمام","arm":"","glow":"التوهج","plug":"شمعة","water":"الماء","in":"في","fuel/water":"وقود/ماء","rail":"السكة","trim":"التعديل","metering":"المعايرة",
"volume":"كمية","mass":"كتلة","absolute":"المطلق","barometric":"الجوي","ambient":"المحيط","evaporator":"المبخر","refrigerant":"الفريون","cruise":"مثبت السرعة","multi-function":"متعدد الوظائف","resume":"استئناف","set":"ضبط","coast":"تخفيف","accelerate":"تسارع",
"starter":"السلف","generator":"الدينمو","terminal":"طرف","field/f":"الحقل","immobilizer":"مانع التشغيل","key":"المفتاح","security":"الأمان","restraints":"الوسائد الهوائية","body":"الهيكل","instrument":"العدادات","panel":"لوحة","cluster":"مجموعة","display":"الشاشة",
"seat":"المقعد","mirror":"المرآة","roof":"السقف","sunroof":"فتحة السقف","headlamp":"المصباح الأمامي","lighting":"الإضاءة","audio":"الصوت","radio":"الراديو","antenna":"الهوائي","amplifier":"المضخّم","telephone":"الهاتف","navigation":"الملاحة","compass":"البوصلة",
"hvac":"التكييف","tire":"الإطار","monitor":"مراقبة","ride":"التعليق","traction":"التماسك","dynamics":"الديناميكا","angle":"زاوية","yaw":"الانحراف","rate":"معدل","lateral":"الجانبي","acceleration":"التسارع","deceleration":"التباطؤ","abs":"ABS","four-wheel":"الدفع الرباعي","4wd":"الدفع الرباعي","four":"الرباعي",
"cooling":"التبريد","cooler":"المبرّد","thermostat":"الثرموستات","heated":"المسخَّن","catalyst":"الدبة","nox":"NOx","hc":"HC","adsorption":"الامتزاز","particulate":"الجسيمات","trap":"الفلتر","filter":"الفلتر","post":"بعدي","ozone":"الأوزون","reduction":"الاختزال",
"dc/dc":"DC/DC","energy":"الطاقة","alternative":"البديل","composition":"تركيب","cap":"الغطاء","reservoir":"الخزان","vapor":"البخار","booster":"المعزّز","servo":"السيرفو","mount":"القاعدة","element":"العنصر","friction":"الاحتكاك","direction":"الاتجاه","digital":"الرقمي",
"multiple":"متعدد","single":"مفرد","random/multiple":"عشوائي/متعدد","contribution/balance":"المساهمة/التوازن","resolution":"الدقة","pulses":"النبضات","pulse":"نبضة","window":"النافذة","time":"زمن","period":"فترة","cycling":"التدوير","status":"الحالة","enable":"تفعيل","disable":"تعطيل",
"wastegate":"بوابة التيربو","boost":"ضغط التيربو","turbo":"التيربو","charger":"الشاحن","overspeed":"سرعة زائدة","overboost":"ضغط تيربو زائد","underboost":"ضغط تيربو ناقص","accessory":"الملحقات","auxiliary":"المساعد","main":"الرئيسي","remote":"عن بُعد","driver":"السائق","occupant":"الراكب",
"a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","x":"X","y":"Y","o2":"الأكسجين","ho2s":"حساس الأكسجين المسخَّن","tcm":"TCM","ecm":"ECM","pcm":"PCM","can":"CAN","egr":"EGR","map/maf":"MAP/MAF","maf":"MAF","vss":"VSS","vin":"VIN","ram":"RAM","rom":"ROM","kam":"KAM","ipc":"IPC","imt":"IMT","rpm":"RPM","prndl":"PRNDL","sae":"SAE",
"and":"و","or":"أو","of":"","the":"","for":"لـ","to":"إلى","at":"عند","with":"مع","from":"من","between":"بين","during":"أثناء","-":"-","/":"/"}
W.update({"deactivation/intake":"الإيقاف/السحب","detected":"","error":"خطأ","management":"إدارة","gate":"البوابة","switching":"التبديل","stop":"الإيقاف","direct":"المباشر","flow/pressure":"التدفق/الضغط","electronics":"الإلكترونيات","resistance":"مقاومة",
"minimum":"الأدنى","maximum":"الأقصى","positive":"الموجب","negative":"السالب","up":"للأعلى","down":"للأسفل","upshift":"النقل للأعلى","downshift":"النقل للأسفل","inhibit":"منع","incompatible":"غير متوافق","programmed":"مبرمج","door":"الباب","restraints":"الوسائد الهوائية",
"cam/rotor/injector":"الكامة/الدوّار/البخاخ","pumping":"الضخ","signals":"إشارات","swapped":"معكوسة","shift/timing":"النقل/التوقيت","deterioration":"تدهور","over-advanced":"متقدم أكثر من اللازم","over-retarded":"متأخر أكثر من اللازم","ignition/distributor":"الإشعال/الموزّع",
"forced":"القسري","airflow":"تدفق الهواء","load":"الحمل","throttle/fuel":"الخانق/الوقود","player/changer":"المشغّل","disc":"الأقراص","assisted":"المساعَد","road":"الطريق","rough":"الوعر","learning":"التعلّم","adaptive":"التكيفي","mechanical":"الميكانيكي","recorder":"مسجّل","event":"الأحداث",
"run":"التشغيل","run/start":"التشغيل/الإقلاع","start":"الإقلاع","distribution":"التوزيع","information":"المعلومات","effort":"الجهد","column":"العمود","cold":"البارد","indicator":"مؤشر","sensing":"استشعار","entertainment":"الترفيه","detection":"كشف","obstacle":"العوائق","shutoff":"القطع",
"delivery":"الإمداد","hardware":"العتاد","conditioner":"المكيف","options":"الخيارات","evaporative":"البخر","condition":"حالة","loop":"الحلقة","operation":"التشغيل","limit":"الحد","sample":"العيّنة","loss":"فقدان","skip":"تخطي"})
SUF = [("Circuit Range/Performance","دائرة {x}: خارج المدى أو أداء غير سليم"),("Circuit Low Input","دائرة {x}: دخل منخفض"),("Circuit High Input","دائرة {x}: دخل مرتفع"),("Circuit Low Voltage","دائرة {x}: جهد منخفض"),("Circuit High Voltage","دائرة {x}: جهد مرتفع"),
("Circuit Slow Response","دائرة {x}: استجابة بطيئة"),("Circuit No Activity Detected","دائرة {x}: لا نشاط"),("Circuit Low","دائرة {x}: إشارة منخفضة"),("Circuit High","دائرة {x}: إشارة مرتفعة"),("Circuit/Open","دائرة {x} مفتوحة أو فيها خلل"),("Circuit Open","دائرة {x} مفتوحة"),
("Circuit Intermittent/Erratic","دائرة {x}: إشارة متقطعة أو مضطربة"),("Circuit Intermittent","دائرة {x}: إشارة متقطعة"),("Circuit Malfunction","خلل في دائرة {x}"),("Circuit Shorted","قصر في دائرة {x}"),("Circuit Performance","دائرة {x}: أداء غير سليم"),("Circuit","خلل في دائرة {x}"),
("Range/Performance","{x}: خارج المدى أو أداء غير سليم"),("Performance or Stuck Off","{x}: أداء غير سليم أو عالق في وضع الإيقاف"),("Stuck Open","{x}: عالق مفتوحاً"),("Stuck Closed","{x}: عالق مغلقاً"),("Stuck On","{x}: عالق في وضع التشغيل"),("Stuck Off","{x}: عالق في وضع الإيقاف"),
("Performance","{x}: أداء غير سليم"),("Intermittent/Erratic","{x}: متقطع أو مضطرب"),("Intermittent","{x}: متقطع"),("Malfunction","خلل في {x}"),("No Signal","{x}: لا إشارة"),("Electrical","{x}: خلل كهربائي"),("Erratic","{x}: مضطرب"),("Too High","{x}: مرتفع جداً"),("Too Low","{x}: منخفض جداً"),
("High","{x}: مرتفع"),("Low","{x}: منخفض"),("Open","{x}: مفتوح"),("Signal","خلل إشارة {x}"),("Control","خلل التحكم في {x}")]
SPECIAL = [(r"^Lost Communication With (.+)$","فقدان الاتصال مع {x}"),(r"^Invalid Data Received From (.+)$","بيانات غير صالحة من {x}"),(r"^Software Incompatibility [Ww]ith (.+)$","عدم توافق البرنامج مع {x}"),
(r"^Cylinder (\d+) Misfire Detected$","تفويت في الأسطوانة {n}"),(r"^Random/Multiple Cylinder Misfire Detected$","تفويت عشوائي أو في أكثر من أسطوانة"),(r"^Cylinder (\d+) Contribution/Balance$","خلل توازن الأسطوانة {n}"),
(r"^System Too Lean$","الخليط فقير (وقود قليل)"),(r"^System Too Rich$","الخليط غني (وقود زائد)"),(r"^System Too Lean at Idle$","الخليط فقير عند السلانسيه"),(r"^System Too Rich at Idle$","الخليط غني عند السلانسيه"),(r"^System Too Lean Off Idle$","الخليط فقير خارج السلانسيه"),(r"^System Too Rich Off Idle$","الخليط غني خارج السلانسيه"),(r"^System Too Lean at Higher Load$","الخليط فقير عند الحمل العالي"),(r"^System Too Rich at Higher Load$","الخليط غني عند الحمل العالي"),
(r"^(.+) Efficiency Below Threshold$","كفاءة {x} أقل من الحد"),(r"^(.+) Correlation$","عدم تطابق قراءات {x}"),(r"^(.+) Incorrect Ratio$","{x}: نسبة غير صحيحة"),(r"^Gear (\d+) Incorrect Ratio$","نسبة الغيار {n} غير صحيحة")]
def norm(v):
    for a,b in FIX.items(): v = v.replace(a,b)
    return re.sub(r"\s+"," ",v).strip()
QUAL = re.compile(r"\((Bank \d+)?\s*,?\s*(Sensor \d+)?\s*\)|-?\s*\bBank (\d+)( Sensor (\d+))?|'([A-Z])'|\"([A-Z])\"")
def phrase(p):
    toks = []; rest = p
    # protect multi-word units
    for i,(en,ar) in enumerate(MW):
        rest = re.sub(r"(?<![A-Za-z])"+re.escape(en)+r"(?![A-Za-z])", f" \x00{i}\x00 ", rest)
    out = []; unk = 0
    for t in rest.split():
        m = re.fullmatch(r"\x00(\d+)\x00", t)
        if m: out.append(MW[int(m.group(1))][1]); continue
        k = t.strip("(),").lower()
        if k in W:
            if W[k]: out.append(W[k])
        elif re.fullmatch(r"[\d\-/]+", k): out.append(k)
        else: out.append(t); unk += 1
    out.reverse()
    return " ".join(out), unk
def tr(desc):
    v = norm(desc); quals = []
    for m in QUAL.finditer(v):
        g = m.group(0)
        b = re.search(r"Bank (\d+)", g); s = re.search(r"Sensor (\d+)", g); l = re.search(r"['\"]([A-Z])['\"]", g)
        if b: quals.append(f"الصف {b.group(1)}")
        if s: quals.append(f"الحساس {s.group(1)}")
        if l: quals.append(l.group(1))
    base = re.sub(r"\s+"," ",QUAL.sub(" ", v)).strip(" -")
    ar = None; unk = 0
    for pat,tpl in SPECIAL:
        m = re.match(pat, base)
        if m:
            g = m.group(1) if m.groups() else ""
            if "{n}" in tpl: ar = tpl.format(n=g)
            elif "{x}" in tpl: x,unk = phrase(g); ar = tpl.format(x=x)
            else: ar = tpl
            break
    if ar is None:
        cm = re.search(r"\s*-?\s*Cylinder (\d+)", base)
        if cm:
            quals.append(f"الأسطوانة {cm.group(1)}"); base = (base[:cm.start()]+" "+base[cm.end():]).strip(" -"); base = re.sub(r"\s+"," ",base)
        if "(" in base or ")" in base: unk = 99
        for suf,tpl in SUF:
            if base.endswith(" "+suf):
                x,u2 = phrase(base[:-len(suf)-1]); unk += u2; ar = tpl.format(x=x); break
        else:
            ar,u2 = phrase(base); unk += u2
    letters = [q for q in quals if len(q)==1]; others = [q for q in quals if len(q)>1]
    if letters:
        L = " " + "/".join(letters)
        ar = ar.replace(":", L+":", 1) if ":" in ar else ar + L
    if others: ar += " (" + "، ".join(others) + ")"
    ar = re.sub(r"التحكم (?!ب|في)(?=\S)", "التحكم بـ", ar)
    return re.sub(r"\s+"," ",ar).strip(), unk
HAND = {"P0128":"الثرموستات: حرارة سائل التبريد أقل من حرارة عمل الثرموستات","P0442":"تسريب صغير في نظام انبعاثات البخر EVAP","P0455":"تسريب كبير في نظام انبعاثات البخر EVAP","P0456":"تسريب صغير جداً في نظام انبعاثات البخر EVAP",
"P0457":"تسريب في نظام EVAP بسبب غطاء الوقود مرتخٍ أو مفقود","P0401":"تدفق إعادة تدوير غاز العادم EGR غير كافٍ","P0402":"تدفق إعادة تدوير غاز العادم EGR زائد","P0700":"نظام التحكم بناقل الحركة يطلب إضاءة لمبة Check Engine","P0730":"نسبة غيار غير صحيحة",
"P0741":"كلتش محوّل العزم: أداء غير سليم أو عالق في وضع الإيقاف","P0440":"خلل في نظام انبعاثات البخر EVAP","P0441":"تدفق تنفيس غير صحيح في نظام EVAP","P0446":"خلل في دائرة التحكم بتهوية نظام EVAP","P0505":"خلل في نظام التحكم بالسلانسيه",
"P0506":"سرعة السلانسيه أقل من المتوقع","P0507":"سرعة السلانسيه أعلى من المتوقع","P0113":"دائرة حساس حرارة هواء السحب: إشارة مرتفعة","P0299":"ضغط التيربو ناقص","P0234":"ضغط التيربو زائد","P0325":"خلل في دائرة حساس الطرق 1 (الصف 1 أو حساس مفرد)",
"P0335":"خلل في دائرة حساس موضع عمود الكرنك A","P0172":"الخليط غني (وقود زائد) (الصف 1)","P0171":"الخليط فقير (وقود قليل) (الصف 1)","P0174":"الخليط فقير (وقود قليل) (الصف 2)","P0175":"الخليط غني (وقود زائد) (الصف 2)","U0121":"فقدان الاتصال مع وحدة التحكم بنظام ABS",
"U0101":"فقدان الاتصال مع وحدة التحكم بناقل الحركة TCM","U0140":"فقدان الاتصال مع وحدة التحكم بالهيكل BCM","U0155":"فقدان الاتصال مع لوحة العدادات","U0073":"ناقل اتصال وحدات التحكم A متوقف","P0420":"كفاءة الدبة (المحوّل الحفاز) أقل من الحد (الصف 1)","P0430":"كفاءة الدبة (المحوّل الحفاز) أقل من الحد (الصف 2)"}
res = {}; unkc = collections.Counter(); bad = 0
for k,v in sorted(d.items()):
    ar,unk = tr(v)
    if k in HAND: ar,unk = HAND[k],0
    res[k] = (ar, v, unk)
    if unk:
        bad += 1
        for t in re.findall(r"[A-Za-z][A-Za-z/\-]+", ar):
            if t.lower() not in ("egr","evap","map","maf","nox","can","tcm","ecm","pcm","abs","bcm","check","engine","dc","hc","p","n","vss","vin","ram","rom","kam","ipc","imt","rpm","prndl","sae","ecm/pcm","dc/dc","map/maf","p/n"): unkc[t]+=1
print(len(res), "partial:", bad); print(unkc.most_common(40))
for k in [] and ["P0010","P0016","P0101","P0128","P0171","P0300","P0304","P0420","P0442","P0455","P0500","P0700","P0730","P0741","P2101","P2135","U0100","U0121","P0135","P0340","P0401","P0562"]: print(k, "|", res[k][0], "|", res[k][1])
json.dump(res, open("dtc_ar.json","w",encoding="utf-8"), ensure_ascii=False)
