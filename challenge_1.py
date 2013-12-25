from morse import decode


# See challenge_1.png
# (r)ed, (g)reen notes
cyphertext = """

rgg g gr grg ggg gr rg r gr r gg\
gg g ggg g rgrg gr\
g g r rgrg rrr r\
gg g gg ggg g gggg\
r rggr gggr gr rgg rrr r \
ggr rgrg rggr grg ggggr g\
grg grg rrr rr rr grg rr rrr \
grg ggg g\

""".replace('r', '-').replace('g', '.')

print decode(cyphertext.strip())
# DEARSANTATHESECRETCODEISE4XVADOTUCXR4FROMMRMORSE
# DEAR SANTA, THE SECRET CODE IS: E4XVA.UCXR4 FROM MR MORSE
# https://cybersecuritychallenge.org.uk/E4XVA.UCXR4/