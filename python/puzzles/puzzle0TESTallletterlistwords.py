poem='''a narrow fellow in the grass
occasionally rides;
you may have met him, did you not,
his notice sudden is.

the grass divides as with a comb,
a spotted shaft is seen;
and then it closes at your feet
and opens further on.

he likes a boggy acre,
a floor too cool for corn.
yet when a child, and barefoot,
i more than once, at morn,

have passed, i thought, a whip-lash
unbraiding in the sun,
when, stooping to secure it,
it wrinkled, and was gone.

several of nature's people
i know, and they know me;
i feel for them a transport
of cordiality;

but never met this fellow,
attended or alone,
without a tighter breathing,
and zero at the bone.'''

pool = dict()
for letter in poem:
    pool[letter] = pool.get(letter,0) + 1
#print pool
#print pool.keys()


print egrep -i "^[^qjx']{10}$" /usr/share/dict/words




