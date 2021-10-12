from accounts.models import Accounts
from .models import Board, Level, Paper, Year, Session, Question

boards_list = ['Edexcel', 'Cambridge']

for board in boards_list:
    board_obj = Board()
    board_obj.name = board
    board_obj.save()

levels_list = ['O', 'AS', 'A']

for level in levels_list:
    level_obj = Level()
    level_obj.name = level
    level_obj.save()


papers_list = ['1123 - English Language', '2210 - Computer Science', '2281 - Economics', '3204 - Bengali', '4024 - Mathematics D', '4037 - Mathematics Additional',
               '5014 - Environmental Management', '5054 - Physics', '5070 - Chemistry', '7010 - Computer Studies', '7094 - Bangladesh Studies', '7110 - Principles of Accounts', '7707 - Accounting']

for paper in papers_list:
    pap_obj = Paper()
    pap_obj.name = paper
    pap_obj.save()

years_list = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013,
              2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001]

for year in years_list:
    year_obj = Year()
    year_obj.name = str(year)
    year_obj.save()


sessions_list = ['Oct Nov', 'May Jun', 'Jan Feb', 'Aug Sep']

for session in sessions_list:
    ses_obj = Session()
    ses_obj.name = session
    ses_obj.save()

post_content1 = {
    "board": Board.objects.get(name="Edexcel"),
    "level": Level.objects.get(name="A"),
    "paper": Paper.objects.get(name="5070 - Chemistry"),
    "year": Year.objects.get(name="2018"),
    "session": Session.objects.get(name="Jan Feb"),
    "author": Accounts.objects.get(username="SirDarknight"),

    "title": "Are two atoms of the same element identical?",

    "slug": "are-two-atoms-identical",

    "excerpt": "No. Two atoms of the same chemical element are typically not identical. First of all, there is a range of possible states that the electrons of an atom can occupy.",

    "content": "Two atoms of the same element can be different if their electrons are in different states. If one copper atom has an electron in an excited state and another copper atom has all of its electrons in the ground state, then the two atoms are different. The excited copper atom will emit a bit of light when the electron relaxes back down to the ground state, and the copper atom already in the ground state will not. Since the states of the electrons in an atom are what determine the nature of the chemical bonding that the atom experiences, two atoms of the same element can react differently if they are in different states. For instance, a neutral sodium atom (say, from a chunk of sodium metal) reacts with water much more violently than an ionized sodium atom (say, from a bit of salt). Chemists know this very well. It's not enough to say what atoms are involved if you want to fully describe and predict a reaction. You have to also specify the ionization/excitation states of the electrons in the atoms. Even if left alone, an atom often does not come with an equal number of protons and electrons.",

    "verified_explanation": "But what if two atoms of the same element both have their electrons in the same states. Then are they identical? No, they are still not identical. Two atoms of the same element and in the same electronic state could be traveling or rotating at different speeds, which affects their ability to chemically bond. Slower moving atoms (such as the atoms in solid iron) have time to form stable bonds, while faster moving atoms (such as the atoms in liquid iron) cannot form such stable bonds. A slow moving tin atom acts differently from a rapidly moving tin atom. But what if two atoms of the same element both have their electrons in the same states, and the atoms are both traveling and rotating at the same speed. Then are they identical? No. Although two such atoms are essentially chemically identical (they will chemically react in the same way), they are not completely identical. There's more to the atom than the electrons. There's also the nucleus. The nucleus of an atom contains neutrons and protons bonded tightly together. The same chemical element can have a different number of neutrons and still be the same element. We refer to the atoms of the same element with different numbers of neutrons as \"isotopes\". While the particular isotope involved does not affect how an atom will react chemically, it does determine how the atom will behave in nuclear reactions. The most common nuclear reaction on earth is radioactive decay. Some isotopes decay very quickly into other elements and emit radiation, while other isotopes do not. If you are doing carbon dating, the fact that a carbon-12 atom is not identical to a carbon-14 atom is essential to the dating process. Simply counting the number of carbon atoms in a sample will not give you any information about the age of a sample. You will have to count the number of different isotopes of carbon instead."
}

post_ob = Question()
post_ob.board = post_content1['board']
post_ob.level = post_content1['level']
post_ob.paper = post_content1['paper']
post_ob.year = post_content1['year']
post_ob.session = post_content1['session']
post_ob.author = post_content1['author']
post_ob.title = post_content1['title']
post_ob.excerpt = post_content1['excerpt']
post_ob.content = post_content1['content']
post_ob.verified_explanation = post_content1['verified_explanation']
post_ob.save()

post_content2 = {
    "board": Board.objects.get(name="Cambridge"),
    "level": Level.objects.get(name="O"),
    "paper": Paper.objects.get(name="5054 - Physics"),
    "year": Year.objects.get(name="2020"),
    "session": Session.objects.get(name="Aug Sep"),
    "author": Accounts.objects.get(username="SirDarknight"),

    "title": "Can radio antennas emit visible light?",

    "slug": "can-radio-visible-light",

    "excerpt": "Yes, radio antennas can emit visible light, but probably not in the way that you're thinking.",

    "content": "If you pump enough energy into a radio antenna, you can heat it up until it glows and emits visible light through the process of thermal radiation. However, a regular radio antenna cannot emit visible light that carries information, similar to how it does with radio waves. There are, however, other devices that can do this.",

    "verified_explanation": "As you may have learned, electromagnetic waves come in many different frequencies, from radio, infrared, visible, and ultraviolet to x-rays and gamma rays. The red light emitted by a glow stick is fundamentally the same as the radio wave emitted by your Wi-Fi router. Both are electromagnetic waves. The red light just has a much higher frequency than the radio wave (the frequency is a measure of how many cycles the wave completes every second). Because they are fundamentally the same, you could be tempted to conclude that you can get a radio antenna to emit controlled visible light by simply cranking up the frequency of the circuit that is driving the antenna. While this makes sense at first glance, the reality of the material properties of antennas gets in the way. A radio antenna works by using electric circuits to push electrons up and down the antenna, causing the electric fields of the electrons to wave up and down as well. These oscillating electric fields then travel away as electromagnetic radio waves. The frequency of the radio wave is equal to the frequency at which you push the electrons up and down the antenna."
}

post_ob = Question()
post_ob.board = post_content2['board']
post_ob.level = post_content2['level']
post_ob.paper = post_content2['paper']
post_ob.year = post_content2['year']
post_ob.session = post_content2['session']
post_ob.author = post_content2['author']
post_ob.title = post_content2['title']
post_ob.excerpt = post_content2['excerpt']
post_ob.content = post_content2['content']
post_ob.verified_explanation = post_content2['verified_explanation']
post_ob.save()

post_content3 = {
    "board": Board.objects.get(name="Cambridge"),
    "level": Level.objects.get(name="AS"),
    "paper": Paper.objects.get(name="5054 - Physics"),
    "year": Year.objects.get(name="2015"),
    "session": Session.objects.get(name="May Jun"),
    "author": Accounts.objects.get(username="SirDarknight"),

    "title": "Do Kirlian photographs show the soul of an organism?",

    "slug": "do-kirlian-photographs",

    "excerpt": "No, Kirlian photographs do not show the soul of an organism. Kirlian photographs show the light that is released by the electrified air surrounding an object when the object is intentionally filled with electricity. ",

    "content": "Non-scientists and pseudo-scientists claim that the patterns of light captured in Kirlian photography are images of the organism's soul, aura, qi, or metaphysical energy field. However, the truth is much more mundane. When electric charge moves quickly enough through air, it rips electrons off of air molecules and gives them energy. When these electrons recombine with the air molecules, they emit their energy in the form of light. For low to medium amounts of electricity, this process is called gas discharge. This is exactly the process at work in neon signs and fluorescent light bulbs. For high amounts of electricity, the physics involved is more violent and the process is called arcing. Examples of arcing include lightning, the sparks created by spark plugs, and the arc created by an arc welder. Lightning bolts, spark plugs, neon signs, and Kirlian photography all share the same root phenomenon: if you run electricity through air quickly enough, the air glows.",

    "verified_explanation": "Typically, gas discharge is stimulated in tubes containing special gases that are held at low pressures. This increases the efficiency of the process. However, gas discharge happens just fine in regular air at normal pressure. In the open air, gas discharge is called corona discharge. When an object that is sitting in the open air is filled with enough electric charge, the electric charge leaks off of the object into the surrounding air. In doing so, the air surrounding the object becomes electrified and glows. Since the air that is closest to the object is the most electrified, the pattern of light that is present in corona discharge takes on the shape of the object that is being electrically charged. While corona discharge sounds exotic and looks mystical, it is in reality just as mundane as fluorescent light bulbs and spark plugs. Since corona discharge is a straight-forward electrical effect, the pattern of light that is created depends on the electrical conductivity of the object, the shape of the object, and the composition and state of the air surrounding the object. It does not depend on the biological vitality of the object or the emotional state of the object. All objects, from nails to pennies, can be made to emit a corona discharge. This fact does not indicate that nails have souls. It just indicates that electricity has been pumped into a nail to the point that the surrounding air has become electrified and glows."
}

post_ob = Question()
post_ob.board = post_content3['board']
post_ob.level = post_content3['level']
post_ob.paper = post_content3['paper']
post_ob.year = post_content3['year']
post_ob.session = post_content3['session']
post_ob.author = post_content3['author']
post_ob.title = post_content3['title']
post_ob.excerpt = post_content3['excerpt']
post_ob.content = post_content3['content']
post_ob.verified_explanation = post_content3['verified_explanation']
post_ob.save()
