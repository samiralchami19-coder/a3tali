out=[]
def src(n,u): out.append(f"#{n}|{u}")
def sec(d,b): out.append(f"@{d}|{b}")
def rows(s,lvl,items,note_first="",dw="T"):
    for i,t in enumerate(items):
        c,m=t[0],t[1]; cause=t[2] if len(t)>2 else ""; who=t[3] if len(t)>3 else dw
        line=[c,m,cause,who,lvl,s]
        if i==0 and note_first: line.append(note_first)
        out.append("|".join(line))
D="سيارة (رسائل الشاشة)"
src("Toyota الرسمي (كتيّب المالك)","https://assets.sia.toyota.com/publications/en/om-x/OM04051U/topics/chapter7/ch07se020405.html")
src("Hyundai الرسمي (كتيّب Tucson 2025)","https://ownersmanual.hyundai.com/full_webhelp/NX4/2025/en_US/idc0a6db6b274.html")
src("Kia الرسمي (كتيّب 2024)","https://ownersmanual.kia.com/full_webhelp/SK3/2024/en_US/topics/t00136.html")
src("AutoUserGuide (Nissan Altima 2022)","https://www.autouserguide.com/nissan/altima/nissan-altima-2022-vehicle-information-display-warnings-and-indicators-user-guide/")
src("LRMan (Freelander 2)","https://lrman.ru/en/freelander/2/electrics/information/message_list")
src("MBCA Star Magazine (مرسيدس)","https://starmagazine.mbca.org/star-article/march-april-2016/tech-session-%E2%80%93-richard-simonds-how-your-mercedes-benz-communicates-you")
src("YOUCANIC (هوندا)","https://www.youcanic.com/honda-dashboard-warning-lights-symbols/")
src("Blackcircles (أودي)","https://www.blackcircles.com/news/audi-dashboard-warning-lights-explained")
S="أوقف السيارة في مكان آمن واتصل بالوكالة"
sec(D,"تويوتا")
rows("Toyota الرسمي (كتيّب المالك)","O",[
("Engine Coolant Temp High","سخونة المحرك","أوقف السيارة في مكان آمن وراجع كتيّب المالك","U"),("Transmission Oil Temp High","سخونة زيت القير",S,"U"),("Oil Pressure Low","ضغط زيت المحرك منخفض",S),
("Braking Power Low","خلل في نظام الفرامل",S),("Smart Key System Malfunction","خلل نظام المفتاح الذكي","راجع الوكالة"),("Shift to P Before Exiting","فُتح الباب والقير ليس على P","ضع القير على P","U"),
("Auto Power OFF to Conserve Battery","انطفأت الكهرباء تلقائياً لحفظ البطارية","شغّل المحرك وارفع دورانه خمس دقائق","U"),("Headlight System Malfunction","خلل في المصابيح الأمامية LED أو النور العالي التلقائي","تُفحص في الوكالة"),
("Engine Oil Level Low","مستوى زيت المحرك منخفض","أضف الزيت أو غيّره","U"),("Engine Stopped Steering Power Low","توقف المحرك وضعف مساعد المقود","أمسك المقود بقوة","U"),
("Maintenance Required Soon","موعد الصيانة الدورية يقترب","","U"),("Maintenance Required Visit Dealer","حان موعد الصيانة الدورية","","U"),("Engine Maintenance Required","خلل في أحد مكونات المحرك","تُفحص في الوكالة"),
("Oil Maintenance Required Soon","موعد تغيير الزيت يقترب","","U"),("Oil Maintenance Required","حان تغيير الزيت والفلتر","","U"),
("Parking Assist Unavailable Sensor Blocked","حساس الركن مغطى","أزل الماء أو الثلج أو الأوساخ","U"),("Parking Assist Unavailable Low Visibility","الكاميرا الخلفية محجوبة","نظف الكاميرا الخلفية","U"),
("System Malfunction Visit Dealer","خلل في نظام أمان","تُفحص السيارة فوراً"),("System Stopped See Owner's Manual","توقف نظام أمان مؤقتاً","افحص البطارية ونظف الحساسات","U"),
("System Stopped Front Camera Low Visibility","رؤية الكاميرا الأمامية محجوبة","نظف الزجاج الأمامي وأزل الضباب","U"),("System Stopped Front Camera Out of Temperature","حرارة الكاميرا خارج نطاق العمل","عدّل حرارة المقصورة بالمكيف","U"),
("System Stopped Front Radar Sensor Blocked","حساس الرادار الأمامي محجوب","نظف الحساس وغطاءه","U"),("System Stopped Front Radar Out of Temperature","حرارة الرادار غير طبيعية","انتظر حتى تعتدل","U"),
("System Stopped Front Radar In Self Calibration","الرادار يعاير نفسه","نظف الحساس وواصل القيادة","N"),("Cruise Control Unavailable","مثبت السرعة غير متاح","اضغط زر مساعد القيادة بقوة","U"),
("Power Tailgate Unavailable Fully Close Manually","الباب الخلفي الكهربائي يحتاج إعادة تهيئة","أغلقه يدوياً بالكامل","U"),("Power Tailgate Unavailable Malfunction","خلل الباب الخلفي الكهربائي","يُفحص في الوكالة")],
"في سيارات المواصفات الخليجية تظهر الرسائل بالعربية أيضاً. النص هنا من كتيّب بالإنجليزية")
sec(D,"هيونداي")
rows("Hyundai الرسمي (كتيّب Tucson 2025)","O",[
("Shift to P","أُطفئ المحرك والقير ليس على P","ضع القير على P ثم أطفئ","U"),("Vehicle is in N","محاولة إطفاء والقير على N","ضع القير على P ثم أطفئ","U"),("Low key battery","بطارية المفتاح الذكي ضعيفة","استبدل بطارية المفتاح","U"),
("Press brake pedal to start engine","ضُغط زر التشغيل دون دواسة الفرامل","اضغط الفرامل ثم الزر","U"),("Key not in vehicle","المفتاح الذكي ليس داخل السيارة والمحرك يعمل","","U"),("Press START button again","فشل التشغيل من أول مرة","اضغط الزر مرة أخرى","U"),
("Press START button with key","المفتاح الذكي لم يُكتشف","اضغط الزر بالمفتاح نفسه","U"),("Check BRAKE SWITCH fuse","فيوز مفتاح الفرامل مفصول","استبدل الفيوز، أو اضغط زر التشغيل 10 ثوانٍ","U"),
("Shift to P or N to start engine","محاولة تشغيل والقير في وضع خاطئ","شغّل على P أو N","U"),("Battery discharging due to external electrical devices","البطارية تفرغ بسبب أجهزة خارجية","افصل الأجهزة الخارجية","U"),
("Low tire pressure","ضغط الإطارات منخفض","","U"),("Low washer fluid","سائل المسّاحات شارف على النفاد","","U"),("Engine overheated","حرارة سائل التبريد تجاوزت 120 مئوية","أوقف السيارة وراجع قسم السخونة في الكتيّب","U"),
("Check headlight","مصباح أمامي لا يعمل","استبدل اللمبة","U"),("Check turn signal","إشارة الانعطاف لا تعمل","استبدل اللمبة","U"),("Check headlight LED","خلل في مصباح LED الأمامي","يُفحص في الوكالة"),
("Check Active Air Flap system","خلل في بوابة الهواء النشطة","يُفحص في الوكالة"),("Check battery","خلل في البطارية المساعدة 12 فولت","تُفحص في الوكالة"),("Check user authentication system","خلل في المفتاح الرقمي أو بصمة الإصبع","يُفحص في الوكالة"),
("Fingerprint authentication is locked out","تجاوز عدد محاولات البصمة","انتظر دقيقة أو استخدم المفتاح","U")])
sec(D,"كيا")
rows("Kia الرسمي (كتيّب 2024)","O",[
("Engine has overheated","حرارة سائل التبريد فوق 120 مئوية","اتبع إجراءات سخونة المحرك","U"),("Low Key Battery","بطارية المفتاح الذكي فارغة","استبدلها","U"),("Press START button while turning wheel","المقود مقفل","حرّك المقود وأنت تضغط زر التشغيل","U"),
("Check Steering Wheel Lock System","خلل في نظام قفل المقود","يُفحص في الوكالة"),("Key not in vehicle","المفتاح الذكي ليس في السيارة","","U"),("Key not detected","المفتاح الذكي لم يُتعرَّف عليه","","U"),
("Low Pressure","ضغط الإطارات منخفض","","U"),("Shift to P or N to start engine","القير ليس على P أو N","","U"),("Press brake pedal to start engine","زر التشغيل يحتاج دواسة الفرامل","","U"),
("Battery discharging due to external electrical devices","جهاز خارجي يستنزف البطارية","افصل الأجهزة الخارجية","U"),("Press START button again","مشكلة في نظام زر التشغيل","اضغط الزر مرة أخرى","U"),("Press START button with key","المفتاح لم يُكتشف عند التشغيل","اضغط الزر بالمفتاح","U"),
("Check Lane Keeping Assist (LKA)","خلل مساعد البقاء في المسار","يُفحص في الوكالة"),("Check High Beam Assist (HBA) system","خلل مساعد النور العالي","يُفحص في الوكالة"),("Check Forward Collision-Avoidance Assist system","خلل نظام تفادي الاصطدام الأمامي","يُفحص في الوكالة"),
("Check Smart Cruise Control System","خلل مثبت السرعة الذكي","يُفحص في الوكالة"),("Check Blind-Spot Collision Warning System","خلل نظام النقطة العمياء","يُفحص في الوكالة"),("Check Driver Attention Warning (DAW) System","خلل نظام تنبيه انتباه السائق","يُفحص في الوكالة"),
("Icy Road Warning","حرارة الطريق تحت 4 مئوية","قُد بحذر","N")])
sec(D,"نيسان")
rows("AutoUserGuide (Nissan Altima 2022)","1",[
("Key Battery Low","بطارية المفتاح الذكي ضعيفة","استبدلها","U"),("Key System Error","خلل في نظام المفتاح الذكي"),("No Key Detected","المفتاح الذكي خارج السيارة","","U"),("Chassis Control System Error","خلل في نظام التحكم بالشاسيه (تثبيت الفرامل التلقائي)"),
("Door/Trunk Open","باب أو صندوق مفتوح","","U"),("Engine Oil Service due now","حان تغيير زيت المحرك","","U"),("Headlight System Error","خلل في نظام المصابيح الأمامية"),("Loose Fuel Cap","غطاء الوقود غير محكم","أحكم إغلاقه","U"),
("Low Fuel","الوقود منخفض","","U"),("Low Washer Fluid","سائل المسّاحات منخفض","","U"),("The power turned off to save the battery","أُطفئ التشغيل تلقائياً لحفظ البطارية","","U"),("Press Brake Pedal","يجب ضغط دواسة الفرامل","","U"),
("Release Parking Brake","فرامل اليد مشدودة والسيارة تتحرك","","U"),("Shift to Park","القير ليس على P","","U"),("Shipping Mode On Push Storage Fuse","وضع الشحن مفعَّل","اضغط فيوز التخزين للداخل","U"),
("Tire Pressure Low – Add Air","ضغط الإطارات منخفض","","U"),("AWD Error","نظام الدفع الكلي لا يعمل كما يجب"),("AWD High Temp. Stop Vehicle","ارتفاع حرارة زيت الدفع الكلي","أوقف السيارة","U"),
("Tire Size Incorrect","فرق كبير بين قطر العجلات الأمامية والخلفية"),("CVT (AT) Malfunction Service now","مشكلة في ناقل الحركة CVT"),("CVT (AT) hot Power reduced","ارتفاع حرارة زيت القير وتخفيض القدرة","خفّف السرعة ودعه يبرد","U"),
("CVT (AT) Stop the vehicle","إيقاف بسبب حرارة ناقل الحركة","أوقف السيارة","U"),("Driver Attention Alert Malfunction","نظام تنبيه السائق لا يعمل"),("Forward Driving Aids temporarily disabled","الحساس الأمامي محجوب، المساعدات معطلة مؤقتاً","نظف مقدمة السيارة","U"),
("Front Sensor blocked","حساس الرادار الأمامي محجوب","","U"),("Malfunction: See Owner's Manual","خلل في قراءة الإشارات أو الفرملة الخلفية التلقائية"),("Not Available System Malfunction","أنظمة متعددة لا تعمل"),
("Parking Sensor Error","خلل في حساسات الركن"),("Steering Assist Alert","المقود غير ممسوك","أمسك المقود","U"),("Unavailable High Cabin Temperature","حرارة المقصورة فوق 40 مئوية","برّد المقصورة","U"),
("Unavailable: Side Radar Obstruction","الرادار الجانبي محجوب","","U")],"من كتيّب Altima 2022 عبر موقع وسيط")
sec(D,"لاند روفر")
rows("LRMan (Freelander 2)","1",[
("BONNET OPEN","غطاء المحرك مفتوح","","U"),("CHECK ALL TYRE PRESSURES","ضغط منخفض في أكثر من إطار","","U"),("DPF FULL","فلتر الجسيمات يحتاج تجديداً","قُد على الطريق السريع فترة","U"),("DPF FULL VISIT DEALER","فشل تجديد فلتر الجسيمات"),
("DSC SWITCHED OFF","نظام الثبات مطفأ","اضغط زر DSC","U"),("ENGINE SYSTEM FAULT","خلل رصده كمبيوتر المحرك"),("FUEL TANK CAP LOOSE OR MISSING","غطاء الوقود مرتخٍ أو مفقود","","U"),
("HDC FAULT SYSTEM NOT AVAILABLE","خلل نظام نزول المنحدرات","بطارية ضعيفة، حساس سرعة عجلة، مفتاح ضوء الفرامل، حساس زاوية المقود، وحدة ABS، أسلاك"),("HDC NOT AVAILABLE IN THIS GEAR","الغيار الحالي لا يناسب HDC","","U"),("HDC NOT AVAILABLE SPEED TOO HIGH","السرعة أعلى من حد HDC","","U"),
("HDC TEMPORARILY NOT AVAILABLE SYSTEM COOLING","HDC متوقف حتى تبرد الفرامل","انتظر","U"),("HIGH ENGINE SPEED FOR COOLING","رفع دوران المحرك لتسريع التبريد","","N"),("LOW COOLANT LEVEL","مستوى سائل التبريد منخفض","افحص التسريب"),
("LOW WASHER FLUID","سائل المسّاحات منخفض","","U"),("OIL SERVICE REQUIRED VISIT DEALER","الزيت تميّع بسبب تجديد الفلتر"),("REDUCED ENGINE PERFORMANCE","قدرة المحرك مخفّضة"),
("SPECIAL PROGRAM TEMPORARILY NOT AVAILABLE","برامج التضاريس متوقفة مؤقتاً","","U"),("TERRAIN RESPONSE SYSTEM FAULTY","خلل محتمل في نظام التضاريس"),("TERRAIN RESPONSE SYSTEM NOT AVAILABLE","نظام التضاريس غير متاح بسبب خلل"),
("TRANSMISSION FAULT","خلل رصده كمبيوتر القير"),("TRANSMISSION FAULT AND OVERHEATING","خلل في القير مع ارتفاع الحرارة"),("TRANSMISSION FAULT LIMITED GEARS AVAILABLE","خلل في القير وغيارات محدودة"),
("TRANSMISSION FAULT TRACTION REDUCED","خلل في القير وتماسك مخفّض"),("TRANSMISSION OVERHEAT SLOW DOWN","حرارة القير مرتفعة","خفّف السرعة أو توقف","U"),("TYRE PRESSURE MONITORING SYSTEM FAULT","خلل نظام مراقبة ضغط الإطارات"),
("TYRE PRESSURES LOW FOR SPEED","ضغط الإطارات منخفض للسرعة العالية","","U"),("FRONT LEFT TYRE PRESSURE NOT MONITORED","لا إشارة من حساس الإطار الأمامي الأيسر"),("AUXILIARY HEATER UNAVAILABLE LOW BATTERY","السخان المساعد متوقف لضعف البطارية")],
"من دليل صيانة Freelander 2، ورسائل الموديلات الأحدث تختلف")
sec(D,"مرسيدس")
rows("MBCA Star Magazine (مرسيدس)","1",[
("ESP","خلل في نظام الثبات الإلكتروني"),("ESP Off","نظام الثبات مطفأ","","U"),("Power Steering","خلل في مساعد المقود"),("Restraint System","مشكلة في الوسائد الهوائية أو أنظمة التقييد"),
("Supplemental Restraint System Service Required","الوسادة الهوائية أو شدّاد الحزام قد لا يعمل"),("Electric Parking Brake","خلل فرامل اليد الكهربائية أو جهد منخفض"),("ABS","خلل نظام منع انغلاق الفرامل"),
("Check Engine","خلل في المحرك أو نظام الانبعاثات"),("BRAKE","خلل في الفرامل أو زيتها منخفض"),("Coolant","المحرك ساخن أو مشكلة في سائل التبريد","أوقف السيارة","U"),
("Battery (أحمر)","عطل نظام الشحن","توقف فوراً","U"),("Engine oil (أحمر)","مستوى زيت المحرك منخفض جداً","","U"),("ABS/ESP/Brake Assist (أصفر)","أنظمة التحكم بالفرامل معطلة","قُد بحذر"),
("Tire Pressure Monitoring","افحص ضغط الإطارات","","U"),("Distance Warning","تنبيه الاقتراب من جسم أمامك","","N"),("Passenger airbag deactivated","وسادة الراكب الأمامي لن تعمل","","N")],"من مقال في مجلة نادي ملّاك مرسيدس")
sec(D,"هوندا")
rows("YOUCANIC (هوندا)","1",[
("ABS","نظام ABS معطل، مسافة التوقف قد تطول"),("Service Engine Soon","مشكلة في المحرك أو الانبعاثات أو القير"),("Air Bag","الوسائد الهوائية معطلة"),("Engine Temperature","سخونة المحرك","توقف وأطفئ المحرك فوراً","U"),
("Tire Pressure Monitor","ضغط منخفض في إطار أو أكثر","","U"),("Charge System","مشكلة في نظام الشحن"),("Oil Warning","ضغط الزيت منخفض","توقف فوراً","U"),("Brake","مشكلة في نظام الفرامل","لا تقُد السيارة"),
("Electronic Power Steering","مشكلة في مساعد المقود الكهربائي"),("Stability Control","نظام الثبات معطل"),("Low Washer Fluid","سائل المسّاحات منخفض","","U"),("Low Fuel","الوقود منخفض","","U"),("Door Ajar","باب غير مغلق تماماً","","U")],"أضواء لوحة العدادات لا رسائل نصية")
sec(D,"أودي")
rows("Blackcircles (أودي)","1",[
("Low Oil Pressure","ضغط الزيت منخفض جداً","افحص المستوى وأضف فوراً","U"),("Coolant Temperature Too High","سخونة المحرك","توقف ودعه يبرد","U"),("Brake System Warning","فرامل اليد مشدودة أو الزيت منخفض أو خلل هيدروليكي"),
("Battery / Charging Fault","الدينمو أو البطارية لا تشحن"),("Airbag / Restraint Fault","خلل محتمل في الوسائد أو شدّادات الأحزمة"),("Steering Lock / Power Steering","مساعد المقود ضعيف أو المقود مقفل"),
("Transmission Fault","مشكلة في قير S tronic أو Tiptronic"),("Pre Sense Fault","خلل نظام الأمان الاستباقي"),("Adaptive Suspension Fault","مشكلة في التعليق الهوائي"),("EPC","مشكلة في دواسة الوقود أو حساسات أو إلكترونيات المحرك","حساس دواسة الوقود، بوابة الخانق متسخة أو عالقة، حساس دواسة الفرامل، بواجي أو كويلات، حساس الكرنك"),
("Check Engine / MIL","خلل في الانبعاثات أو الإشعال أو الوقود"),("ABS / ESC / Traction","أنظمة الأمان معطلة"),("Brake Pad Wear","فحمات الفرامل متآكلة","استبدلها قريباً","U"),("Tyre Pressure Monitoring","ضغط إطار منخفض أو خلل في النظام","","U"),
("DPF Warning","الفلتر مسدود أو فشل التجديد","قُد على سرعة الطريق السريع","U"),("Driver Assistance Faults","مثبت السرعة أو مساعد المسار أو حساسات الركن لا تعمل"),("AdBlue Warning","سائل AdBlue منخفض","املأه قبل أن تمتنع السيارة عن التشغيل","U"),
("Bulb Failure","لمبة أو أكثر لا تعمل","","U")],"أضواء ورسائل عامة")
open("data/15_cars.txt","w",encoding="utf-8").write("\n".join(out)+"\n")
