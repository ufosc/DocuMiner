from textblob import TextBlob

#testing the sentiment analysis
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
sentence = "Textblob is amazingly simple to use. What great fun!"
paragraph1 = """Robert is a motivated and conscientious employee who takes pride in his work.
                Robert would benefit, however, from organizing his time more efficiently.
                He occasionally fails to prioritize important pieces of work and instead spends a
                large amount of time on projects that are not in alignment with our departmental goals.
                During this next review period, I would like to see him establish specific and relevant
                personal goals to help him focus and stay on track in the context of wider objectives within our organization."""
paragraph2 = """According to Holli Riebeek, the author of “Global Warming,” nature also contribute to
                climate change by emitting CO2 from volcanos. Don Wuebbles, a coordinating lead author and
                contributor to a number of the reports of the International Intergovernmental Panel on Climate
                Change (IPCC), which was awarded the Nobel Peace Prize in 2007, and a Professor of
                Atmospheric Sciences at the University of Illinois at Urbana-Champaign, stated, “Volcanos used
                to release CO2 many millions years ago. Back where dinosaurs existed, we had levels of CO2
                that is approximately similar to what we have now because of the CO2 emitted by volcanos."""
paragraph3 = """According to the EPA, wind power is the fastest-growing energy resources in the world
                since 1990. Since wind turbines use the wind, a renewable source of energy, to generate
                electricity it has little to no impact on the environment (EPA). Furthermore, wind turbines don’t
                need water to operate (EPA). According to the U.S. Department of Energy, the usage of wind
                turbines cut water consumption in the power sector by 36.5 billion gallons in 2013 alone. Also,
                the usage of wind turbines in 2013 reduced CO2 emission approximately by 115 million metric
                tons, which equals the emission of 20 million cars during the year (Wind Energy Benefits).
                However, there are some challenges that face wind power. One main challenge is that
                birds and bats have been killed from flying into the spinning blades. However, to help solve the
                problem of birds and bats getting killed by the spinning blades, one solution is to avoid building
                wind turbines in areas where there is a high concentration of migrants. Another solution is to
                make the wind turbines blades rotate only above certain wind speed. Researchers have found
                that when wind speed is over 15 mph, 99% of bat activity has stopped in some areas (How to
                Make Wind Power More Wildlife Friendly 19)."""

#taken from example essay
document = """ Abstract
    Climate change has become a widespread topic in recent years. This a problem that resulted
    from the emission of greenhouse gases that affect our environment. Therefore, it raises
    questions on whether the problem is caused by human activities or it’s just a part of nature’s
    cycle. This paper discusses and compares the factors that contribute to climate change by
    humans and nature, some effects of climate change, and some solutions that have been
    developed to prevent or slow climate change from progressing.
    Climate Change
    According to NASA, the Earth average temperature has increased about 1 degree
    Fahrenheit during the 20th century (Global Climate Change: Effects). That might sound like it
    isn’t a great change, but its effects on our environment have proven otherwise. The impacts of
    this small change in the temperature are many, from longer drought seasons and heat waves to
    more aggressive hurricanes (Global Climate Change: Effects). Furthermore, the increase in the
    earth’s average temperature created a variety of problems that left a lasting scar on our
    environment (Global Climate Change: Effects).
    Jamil 2
    Causes
    Greenhouse Gases
    Greenhouse gases are thought to be the main contributor to climate change (The
    Greenhouse Effect). They are very efficient in trapping heat into the atmosphere; therefore, it
    results in the greenhouse effect.
    The solar energy is absorbed by the earth’s surface and then reflected back to the
    atmosphere as heat. Then as the heat goes out to space, greenhouse gases absorb a part of the
    heat. After that, they radiate the heat back to the earth’s surface, to another greenhouse gas
    molecule, or to space (The Greenhouse Effect). Daniela Burghila et al. stated in “Climate
    Change Effects- Where to Next?”, the biggest concern scientists have is about the emission of
    CO2 since it is about 75% of the total global emission of greenhouse gases (406).
    Methane and CO2
    According to L.A. Berbisi et al. in “Methane leakage from evolving petroleum systems:
    Masses, rates and inferences for climate feedback,” the present-day warming trend has been
    attributed to an annual increase in the atmospheric methane concentration andCO2 (225). The
    Berbisi et al. study also investigated the potential of methane contribution to the atmosphere
    during the evolution of petroleum system in two different geological settings: The western
    Canada sedimentary basin and the Central Graben area of the North Sea. Numerical simulation
    and different types of mass balance (conversion of mass to the analysis of physical systems) as
    well as theoretical approaches were applied. In western Canada sedimentary basin case,
    maximum thermogenic methane leakage rates in the order of 10-2
    -10-3 and maximum biogenic
    Jamil 3
    methane generation rates of 10-2 Tg/yr were estimated. In the Central Graben case there was
    an estimate of maximum thermogenic methane leakage in order of 10-3 Tg/yr. Applying the
    results to a global scale shows that thermal gas generation in hydrocarbon, single process
    kitchen area would not influence climate (227). On the other hand, only the sudden release of
    surface methane accumulations, formed over geological time scales, petroleum systems can
    influence climate (219).
    The following chemical equations demonstrate the production of each (Global Climate
    Change: Human Influences-- The Chemistry):
    Combustion of fossil fuels:
    6 O2 + C6H12O6 --------> 6 H2O + 6 CO2 + energy
    Production of methane during microbial metabolic process:
    CH3COOH --------> CO2 + CH4
    Nature Contributions
    According to Holli Riebeek, the author of “Global Warming,” nature also contribute to
    climate change by emitting CO2 from volcanos. Don Wuebbles, a coordinating lead author and
    contributor to a number of the reports of the International Intergovernmental Panel on Climate
    Change (IPCC), which was awarded the Nobel Peace Prize in 2007, and a Professor of
    Atmospheric Sciences at the University of Illinois at Urbana-Champaign, stated, “Volcanos used
    to release CO2 many millions years ago. Back where dinosaurs existed, we had levels of CO2
    that is approximately similar to what we have now because of the CO2 emitted by volcanos.
    Jamil 4
    But, volcanos release a small amount of CO2 and they can’t explain the increase of CO2 that we
    had in the last century” (Phone interview).
    Volcanos do contribute to climate change by emitting CO2. However, the amount of CO2
    they emit is relatively small if we compare it to the amount of CO2 that is being released by
    human activities. According to NASA, on average, volcanoes emit between 130 and 230 million
    tons of CO2 per year. However, by burning fossil fuels, people release in excess of 100 times
    more, about 26 billion tons of CO2, into the atmosphere every year (as of 2005) (rIEBEEK).
    Human Contributions
    Scientists believe humans’ activities contribute to climate change because we depend
    on fossil fuels for our energy needs (Riebeek). Wuebbles said, “A large amount of climate
    change happens widely because we are burning fossil fuels and that increases gases such as
    CO2, methane, and some other gases in the atmosphere” (phone interview). According to the
    Australian Greenhouse Office, the world depends on fossil fuels such as oil, coal, and natural
    gas for 80% of its energy needs. Therefore, that makes it very hard to switch from fossil fuels to
    any other forms of energy because we depend on fossil fuels to a large degree. The emission of
    greenhouse gases has increased dramatically from the industrial revolution, mostly from the
    burning of fossil fuels for energy, agriculture, industrial process, and transportation (Ecological
    Impacts of Climate Change). The graph on the next page shows how much CO2 and methane
    increased in the last 250 years.
    Jamil 5
    Source: (“Climate Change” graph done by Robert Simmon.)
    The graph was done by taking a sample of ice and another sample was taken from the
    atmosphere. For the ice sample, drilling a hole through the ice sheets and looking at the air
    molecules inside the sample determined the concentration of CO2 and methane (Chasing Ice).
    The graph illustrates that carbon dioxide levels have increased nearly 38 percent from 1750-
    2009 and methane levels have increased 148 percent (Riebeek).
    Effects of Climate Change
    Climate change has affected many aspects of our planet. One aspect that has been
    greatly affected by climate change is the weather. In Romania, for instance, extreme weather
    events have multiplied since 2002. Burghila et al. stated in “Climate Change Effects- Where to
    Next?”, that the country’s 2007 drought was the severest in 60 years (408). By increasing the
    concentration of the greenhouse gases, we are increasing the amount of heat that is in our
    atmosphere (NASA). Hurricanes have also become more aggressive largely because of warmer
    Jamil 6
    temperatures that mainly resulted from the emission of greenhouse gases. Warmer
    temperatures result in warmer water in the oceans. As the result of warmer oceans, hurricanes
    and tornados become more intense. Wuebbles stated, “Warmer atmosphere result in more
    energy in the atmosphere. When hurricanes start, they usually pick up energy from the oceans
    and as the result of warmer water in the oceans because of greenhouse effect, hurricanes have
    more energy. Therefore, hurricanes become more intense. Now if the water was colder that
    gives less energy to hurricanes and make it less intense” (phone interview). Also, warmer
    temperature means the atmosphere holds more water vapor and that makes rainfalls more
    extreme and intense (Riebeek).
    Climate change also resulted in playing a major role in shrinking of ice sheets (Riebeek).
    The melting of ice results in the rise of sea levels and that endangers many islands to disappear
    completely (Riebeek). According to NASA, up to 10 percent of the world’s population lives in
    areas where there about 30 feet above sea level (NASA). Furthermore, Greenland and West
    Antarctic ice sheets are melting about 125 billion tons of ice per year (Riebeek). Wuebbles said,
    “As the earth warming its leading to melting more ice and glaciers. We could see as much as 6
    feet sea level rise in this century” (Phone interview).
     According to Weiwei Mo, Haiying Wang, Jennifer M. Jacobs in “Understanding the
    influence of climate change on the embodied” the energy of water supply is commonly
    perceived that climate change has a negative impact on water quantity and quality as well as
    drinking water treatment. However, some issues such as, geographical locations, local water
    resources, and water technologies that could potentially influence the effect of climate change
    on drinking water supply are still unsettled (221).
    Jamil 7
     Weiwei, Haiying, and Jacobs also stated that their study was performed on a selected
    water supply system located in northeast US. Multivariate regression analyses were
    implemented to test the statistical correlation, among monthly life cycle energy consumptions,
    three indicators of water quality (UV254, PH and water temperature) and five climate indicators
    (monthly mean temperature, monthly mean maximum/minimum temperature, total
    precipitation, and total snow fall) (221).
     The study also concluded that most of the variations in chemical and energy uses were
    attributed to water quality and climate variations except for the use of soda ash. The study also
    found that future climate change might slightly reduce energy and chemical uses under both
    the highest emission and the lowest emission levels generated by the intergovernmental panel
    on climate change (IPCC). Another major finding of this study that the effects of climate change
    on the volumetric life cycle energy use in the water supply (reduction by 3-6%) could outweigh
    the increase in demand for water due to a warmer climate in the case of study system by the
    end of the century (225,227,229).
     Findings of this study reveal the importance of considering factors, such as geographical
    locations, local environment, water treatment technologies, and water resource management,
    on appreciating and identifying the potential impact of climate change on the quantity and the
    quality of drinking water (229).
    Jamil 8
    Solutions
    There have been many debates and discussions on how to combat climate change
    among nations. However, many factors influence on whether the solutions are efficient
    economically or it cost too much to maintain. The following solutions are considered among the
    efficient solutions to reduce the progress of climate change:
    1. Wind power
    According to the EPA, wind power is the fastest-growing energy resources in the world
    since 1990. Since wind turbines use the wind, a renewable source of energy, to generate
    electricity it has little to no impact on the environment (EPA). Furthermore, wind turbines don’t
    need water to operate (EPA). According to the U.S. Department of Energy, the usage of wind
    turbines cut water consumption in the power sector by 36.5 billion gallons in 2013 alone. Also,
    the usage of wind turbines in 2013 reduced CO2 emission approximately by 115 million metric
    tons, which equals the emission of 20 million cars during the year (Wind Energy Benefits).
     However, there are some challenges that face wind power. One main challenge is that
    birds and bats have been killed from flying into the spinning blades. However, to help solve the
    problem of birds and bats getting killed by the spinning blades, one solution is to avoid building
    wind turbines in areas where there is a high concentration of migrants. Another solution is to
    make the wind turbines blades rotate only above certain wind speed. Researchers have found
    that when wind speed is over 15 mph, 99% of bat activity has stopped in some areas (How to
    Make Wind Power More Wildlife Friendly 19).
    Jamil 9
    2. Green Buildings
    Existed buildings emit CO2 because of their dependence on fossil fuels for energy from
    air-conditioning to electricity (Energy–Efficient Buildings). Furthermore, the buildings that we
    live and work account for 30% of all greenhouse gases emissions in the United States (Energy–
    Efficient Buildings). Using light bulbs that use less energy and more efficient heating and cooling
    systems helps in reducing the amount of CO2 that is being emitted from the buildings (Energy–
    Efficient Buildings). Therefore, that reduces our dependency on fossil fuel for electricity
    resulting in a reduction of greenhouse gases emission (Energy–Efficient Buildings).
     For instance, the Empire State Building in New York went through renovations to improve
    energy efficiency. The renovations have reduced energy usage by 38% and save 4.4 million
    dollars on heating and electricity bills each year (Energy–Efficient Buildings).
    3. Methane Leaks
    As it has been mentioned above, that Methane is a greenhouse gas that contributes to
    the progress of climate change. Natural gas and petroleum systems are also considered, among
    the main sources of methane emission. Upgrading the equipment used in transferring, storing,
    and producing oil and gas can limit methane leaks (Overview of Greenhouse Gases).
    Solutions undergoing research
    According to Li, Bo Zou, Changwen in “Nitrogen-doped Porous Carbon Nanofiber Webs
    for Efficient CO2 Capture and Conversion” there have been two ways developed to try to solve
    the excess amount of CO2 that is being released from using fossil fuels. Both solutions are
    aimed to capture CO2 from the air and turn it into a usable material. The first solution is called
    Jamil 10
    chemical absorption (79). Using amine-ammonia aqueous solution to capture as much CO2 as
    possible. The process is done by an absorber and a stripper. First, the gas containing CO2 flows
    through a tube or a pipe and it contacts a CO2 absorbent that is flowing in the opposite
    direction. After absorption, the absorbent that is filled with CO2 flows into a stripper for
    thermal regeneration. According to Yu, Cheng-Hsiu, Chih-Hung Huang, and Chung-Sung Tan in
    “A Review of CO2 Capture by Absorption and Adsorption” the pure CO2 that has been released
    are compressed for transportation and storage (746). However, the process’s high cost of
    regeneration, toxicity, the corrosion of equipment, and its low capacity to capture CO2 are
    major setbacks for the process unless improved (79).
     Li, Bo Zou, Changwen in “Nitrogen-doped Porous Carbon Nanofiber Webs for Efficient
    CO2 Capture and Conversion” also stated, the second solution is called adsorption. Several solid
    adsorbents have been developed to better capture CO2 such as zeolites, mesoporous silica,
    microporous organic polymers, metal-organic frameworks (MOFS), and porous carbons.
    However, carbon based materials are the most efficient because of low cost, wide availability,
    thermal and chemical stability, large specific surface area and pore volume, easy-to-design pore
    structure, surface functionalization and low energy consumption for regeneration. However, it
    has low capacity to capture CO2.These solid adsorbents can better capture CO2 by either
    temperature, pressure, or the combination of both (80).
    Conclusion
    Climate change is a problem that is facing our planet and it has progressed a lot after
    the industrial revolution. The emission of greenhouse gases has accelerated the progress of
    climate change and made our weather more intense. However, the world’s dependence on
    Jamil 11
    fossil fuel for energy, transportation, and manufacturing have created a major obstacle for us to
    switch to renewable energy. I would like to conclude with what Dr. Wuebbles mentioned
    regarding the solutions that have been developed to prevent climate change from progressing,
    he said, “We need to transfer our energy to renewable energy. Also, one of the things we must
    do is to adapt to the changes that occurred and will occur. We need to prevent any future
    changes from happening, but adaptation is a major thing we need to do” (Phone interview).
    Scientists, environmentalists, communities, as well as policy makers need to diligently and
    cooperatively to live up to these challenges and combat climate change. """


#functions that return objectivity for different amounts of data
#0.0 is very objective and 1.0 is very subjective

#for a single sentence
def sentenceSubjectivity(mySentence):
    str = TextBlob(mySentence)
    return str.sentiment.subjectivity

#computes average subjectivity of n number of paragraphs
def avgSubjectivity(paragraphs):
    average = 0.0;
    for x in paragraphs:
        str = TextBlob(x)
        curr = str.sentiment.subjectivity
        average += curr
    average /= len(paragraphs)
    return average

#test print statement
print("Doccument subjectivity score: ", sentenceSubjectivity(document))
print("\n")

#tests weighted average of subjectivity of three paragraphs from the doccument
print("Paragraph 1 subjectivity score: ", sentenceSubjectivity(paragraph1))
print("Paragraph 2 subjectivity score: ", sentenceSubjectivity(paragraph2))
print("Paragraph 3 subjectivity score: ", sentenceSubjectivity(paragraph3))
print("\n")
ps = []
ps.append(paragraph1)
ps.append(paragraph2)
ps.append(paragraph3)
print("Average subjectivity of paragraphs 1,2, and 3: ", avgSubjectivity(ps))

print("Exit Program")
