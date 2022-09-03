# My little script to generate a language file for Minecraft
# with all the enchantment levels possible.

out = ""

for ench in range(1, 32768):
    out += "enchantment.level.%s=%s\n" % (ench, ench)

ofile = open("en-us.lang", "w")
ofile.write(out)
ofile.close()