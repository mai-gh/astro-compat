an old small project from may 2020 I found on an old hard drive

# Astro-Compat

parse the data of astrological sign compatability according to https://www.zodiacsign.com/compatibility/

then show compatability of all signs in relation to the provided sign

```
./astro-compat.sh aries
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Feb 19 - Mar 20	    water	pisces      	20%		1%		70%		5%		35%		40%		29%		aries
Dec 22 - Jan 19	    earth	capricorn   	5%		99%		20%		1%		60%		40%		38%		aries
Aug 23 - Sep 22	    earth	virgo       	10%		70%		30%		20%		50%		70%		42%		aries
Jun 21 - Jul 22	    water	cancer      	70%		50%		20%		70%		40%		30%		47%		aries
Oct 23 - Nov 21	    water	scorpio     	50%		90%		20%		1%		40%		99%		48%		aries
Sep 23 - Oct 22	    air  	libra       	80%		40%		55%		99%		70%		30%		62%		aries
Apr 20 - May 20	    earth	taurus      	65%		85%		40%		60%		90%		40%		63%		aries
Jan 20 - Feb 18	    air  	aquarius    	65%		85%		90%		40%		30%		99%		68%		aries
May 21 - Jun 20	    air  	gemini      	90%		40%		85%		60%		75%		50%		74%		aries
Mar 21 - Apr 19	    fire 	aries       	65%		55%		85%		75%		95%		95%		75%		aries
Jul 23 - Aug 22	    fire 	leo         	90%		60%		90%		99%		95%		65%		83%		aries
Nov 22 - Dec 21	    fire 	sagittarius 	95%		70%		90%		90%		70%		99%		87%		aries
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh taurus
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Jan 20 - Feb 18	    air  	aquarius    	15%		20%		10%		15%		1%		5%		11%		taurus
May 21 - Jun 20	    air  	gemini      	5%		10%		60%		35%		1%		25%		23%		taurus
Jul 23 - Aug 22	    fire 	leo         	50%		60%		5%		20%		1%		40%		29%		taurus
Nov 22 - Dec 21	    fire 	sagittarius 	25%		5%		50%		25%		60%		20%		31%		taurus
Sep 23 - Oct 22	    air  	libra       	35%		30%		5%		25%		40%		65%		33%		taurus
Mar 21 - Apr 19	    fire 	aries       	65%		85%		40%		60%		90%		40%		63%		taurus
Aug 23 - Sep 22	    earth	virgo       	85%		75%		90%		85%		50%		55%		73%		taurus
Apr 20 - May 20	    earth	taurus      	95%		75%		50%		99%		95%		99%		86%		taurus
Feb 19 - Mar 20	    water	pisces      	99%		80%		95%		99%		85%		70%		88%		taurus
Dec 22 - Jan 19	    earth	capricorn   	85%		99%		85%		90%		90%		85%		89%		taurus
Oct 23 - Nov 21	    water	scorpio     	95%		80%		75%		99%		99%		85%		89%		taurus
Jun 21 - Jul 22	    water	cancer      	95%		99%		80%		99%		80%		90%		91%		taurus
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh gemini
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Feb 19 - Mar 20	    water	pisces      	15%		1%		20%		1%		5%		15%		10%		gemini
Dec 22 - Jan 19	    earth	capricorn   	1%		50%		25%		1%		5%		10%		15%		gemini
Oct 23 - Nov 21	    water	scorpio     	1%		5%		20%		1%		20%		40%		15%		gemini
Jun 21 - Jul 22	    water	cancer      	5%		25%		70%		10%		1%		15%		21%		gemini
Apr 20 - May 20	    earth	taurus      	5%		10%		60%		35%		1%		25%		23%		gemini
Aug 23 - Sep 22	    earth	virgo       	5%		1%		80%		55%		70%		30%		40%		gemini
Mar 21 - Apr 19	    fire 	aries       	90%		40%		85%		60%		75%		50%		74%		gemini
Sep 23 - Oct 22	    air  	libra       	80%		95%		60%		90%		55%		85%		78%		gemini
Jul 23 - Aug 22	    fire 	leo         	90%		45%		95%		85%		99%		80%		82%		gemini
May 21 - Jun 20	    air  	gemini      	80%		50%		99%		70%		99%		99%		83%		gemini
Jan 20 - Feb 18	    air  	aquarius    	85%		90%		99%		40%		95%		99%		85%		gemini
Nov 22 - Dec 21	    fire 	sagittarius 	90%		99%		99%		95%		70%		99%		92%		gemini
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh cancer
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
May 21 - Jun 20	    air  	gemini      	5%		25%		70%		10%		1%		15%		21%		cancer
Nov 22 - Dec 21	    fire 	sagittarius 	40%		1%		60%		10%		45%		5%		27%		cancer
Sep 23 - Oct 22	    air  	libra       	40%		30%		50%		15%		20%		10%		28%		cancer
Jul 23 - Aug 22	    fire 	leo         	30%		50%		10%		45%		1%		35%		29%		cancer
Jan 20 - Feb 18	    air  	aquarius    	1%		35%		55%		50%		10%		25%		31%		cancer
Mar 21 - Apr 19	    fire 	aries       	70%		50%		20%		70%		40%		30%		47%		cancer
Feb 19 - Mar 20	    water	pisces      	85%		70%		85%		99%		25%		70%		72%		cancer
Aug 23 - Sep 22	    earth	virgo       	95%		99%		60%		65%		50%		90%		77%		cancer
Oct 23 - Nov 21	    water	scorpio     	90%		95%		99%		70%		25%		95%		79%		cancer
Dec 22 - Jan 19	    earth	capricorn   	99%		99%		70%		75%		70%		90%		84%		cancer
Jun 21 - Jul 22	    water	cancer      	65%		99%		90%		99%		99%		55%		85%		cancer
Apr 20 - May 20	    earth	taurus      	95%		99%		80%		99%		80%		90%		91%		cancer
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh leo
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Feb 19 - Mar 20	    water	pisces      	1%		1%		35%		15%		20%		10%		14%		leo
Dec 22 - Jan 19	    earth	capricorn   	5%		40%		60%		1%		50%		5%		27%		leo
Apr 20 - May 20	    earth	taurus      	50%		60%		5%		20%		1%		40%		29%		leo
Jun 21 - Jul 22	    water	cancer      	30%		50%		10%		45%		1%		35%		29%		leo
Oct 23 - Nov 21	    water	scorpio     	5%		65%		30%		1%		35%		40%		29%		leo
Aug 23 - Sep 22	    earth	virgo       	5%		65%		50%		1%		35%		55%		35%		leo
Nov 22 - Dec 21	    fire 	sagittarius 	99%		80%		85%		80%		65%		40%		75%		leo
Sep 23 - Oct 22	    air  	libra       	90%		40%		85%		99%		75%		60%		75%		leo
Jul 23 - Aug 22	    fire 	leo         	50%		70%		65%		90%		99%		85%		78%		leo
May 21 - Jun 20	    air  	gemini      	90%		45%		95%		85%		99%		80%		82%		leo
Mar 21 - Apr 19	    fire 	aries       	90%		60%		90%		99%		95%		65%		83%		leo
Jan 20 - Feb 18	    air  	aquarius    	99%		75%		90%		99%		80%		90%		89%		leo
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh virgo
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Jan 20 - Feb 18	    air  	aquarius    	1%		50%		40%		35%		30%		25%		30%		virgo
Sep 23 - Oct 22	    air  	libra       	1%		25%		60%		1%		30%		65%		30%		virgo
Nov 22 - Dec 21	    fire 	sagittarius 	30%		1%		65%		10%		50%		35%		32%		virgo
Jul 23 - Aug 22	    fire 	leo         	5%		65%		50%		1%		35%		55%		35%		virgo
May 21 - Jun 20	    air  	gemini      	5%		1%		80%		55%		70%		30%		40%		virgo
Mar 21 - Apr 19	    fire 	aries       	10%		70%		30%		20%		50%		70%		42%		virgo
Aug 23 - Sep 22	    earth	virgo       	30%		70%		99%		25%		80%		85%		65%		virgo
Apr 20 - May 20	    earth	taurus      	85%		75%		90%		85%		50%		55%		73%		virgo
Oct 23 - Nov 21	    water	scorpio     	65%		90%		99%		75%		70%		55%		76%		virgo
Dec 22 - Jan 19	    earth	capricorn   	65%		99%		90%		65%		80%		65%		77%		virgo
Jun 21 - Jul 22	    water	cancer      	95%		99%		60%		65%		50%		90%		77%		virgo
Feb 19 - Mar 20	    water	pisces      	99%		65%		85%		95%		75%		99%		86%		virgo
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh libra
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Jun 21 - Jul 22	    water	cancer      	40%		30%		50%		15%		20%		10%		28%		libra
Feb 19 - Mar 20	    water	pisces      	50%		1%		5%		15%		60%		40%		29%		libra
Oct 23 - Nov 21	    water	scorpio     	45%		1%		55%		25%		10%		35%		29%		libra
Aug 23 - Sep 22	    earth	virgo       	1%		25%		60%		1%		30%		65%		30%		libra
Apr 20 - May 20	    earth	taurus      	35%		30%		5%		25%		40%		65%		33%		libra
Dec 22 - Jan 19	    earth	capricorn   	15%		80%		35%		1%		50%		25%		34%		libra
Mar 21 - Apr 19	    fire 	aries       	80%		40%		55%		99%		70%		30%		62%		libra
Jan 20 - Feb 18	    air  	aquarius    	90%		85%		40%		80%		50%		65%		68%		libra
Sep 23 - Oct 22	    air  	libra       	65%		35%		80%		50%		99%		80%		68%		libra
Nov 22 - Dec 21	    fire 	sagittarius 	90%		5%		85%		99%		75%		70%		71%		libra
Jul 23 - Aug 22	    fire 	leo         	90%		40%		85%		99%		75%		60%		75%		libra
May 21 - Jun 20	    air  	gemini      	80%		95%		60%		90%		55%		85%		78%		libra
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh scorpio
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
May 21 - Jun 20	    air  	gemini      	1%		5%		20%		1%		20%		40%		15%		scorpio
Jul 23 - Aug 22	    fire 	leo         	5%		65%		30%		1%		35%		40%		29%		scorpio
Sep 23 - Oct 22	    air  	libra       	45%		1%		55%		25%		10%		35%		29%		scorpio
Jan 20 - Feb 18	    air  	aquarius    	40%		1%		50%		1%		30%		60%		30%		scorpio
Nov 22 - Dec 21	    fire 	sagittarius 	25%		1%		80%		10%		35%		30%		30%		scorpio
Mar 21 - Apr 19	    fire 	aries       	50%		90%		20%		1%		40%		99%		48%		scorpio
Dec 22 - Jan 19	    earth	capricorn   	60%		90%		70%		35%		30%		99%		64%		scorpio
Oct 23 - Nov 21	    water	scorpio     	65%		40%		70%		55%		90%		75%		66%		scorpio
Aug 23 - Sep 22	    earth	virgo       	65%		90%		99%		75%		70%		55%		76%		scorpio
Jun 21 - Jul 22	    water	cancer      	90%		95%		99%		70%		25%		95%		79%		scorpio
Feb 19 - Mar 20	    water	pisces      	70%		65%		90%		99%		75%		85%		81%		scorpio
Apr 20 - May 20	    earth	taurus      	95%		80%		75%		99%		99%		85%		89%		scorpio
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh sagittarius
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Jun 21 - Jul 22	    water	cancer      	40%		1%		60%		10%		45%		5%		27%		sagittarius
Oct 23 - Nov 21	    water	scorpio     	25%		1%		80%		10%		35%		30%		30%		sagittarius
Apr 20 - May 20	    earth	taurus      	25%		5%		50%		25%		60%		20%		31%		sagittarius
Aug 23 - Sep 22	    earth	virgo       	30%		1%		65%		10%		50%		35%		32%		sagittarius
Dec 22 - Jan 19	    earth	capricorn   	5%		10%		75%		55%		20%		60%		38%		sagittarius
Feb 19 - Mar 20	    water	pisces      	30%		1%		85%		30%		65%		90%		50%		sagittarius
Sep 23 - Oct 22	    air  	libra       	90%		5%		85%		99%		75%		70%		71%		sagittarius
Nov 22 - Dec 21	    fire 	sagittarius 	65%		99%		99%		10%		99%		70%		74%		sagittarius
Jul 23 - Aug 22	    fire 	leo         	99%		80%		85%		80%		65%		40%		75%		sagittarius
Jan 20 - Feb 18	    air  	aquarius    	80%		60%		99%		85%		90%		85%		83%		sagittarius
Mar 21 - Apr 19	    fire 	aries       	95%		70%		90%		90%		70%		99%		87%		sagittarius
May 21 - Jun 20	    air  	gemini      	90%		99%		99%		95%		70%		99%		92%		sagittarius
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh capricorn
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
May 21 - Jun 20	    air  	gemini      	1%		50%		25%		1%		5%		10%		15%		capricorn
Jul 23 - Aug 22	    fire 	leo         	5%		40%		60%		1%		50%		5%		27%		capricorn
Sep 23 - Oct 22	    air  	libra       	15%		80%		35%		1%		50%		25%		34%		capricorn
Jan 20 - Feb 18	    air  	aquarius    	5%		80%		65%		5%		40%		25%		37%		capricorn
Mar 21 - Apr 19	    fire 	aries       	5%		99%		20%		1%		60%		40%		38%		capricorn
Nov 22 - Dec 21	    fire 	sagittarius 	5%		10%		75%		55%		20%		60%		38%		capricorn
Dec 22 - Jan 19	    earth	capricorn   	40%		80%		65%		30%		80%		75%		62%		capricorn
Oct 23 - Nov 21	    water	scorpio     	60%		90%		70%		35%		30%		99%		64%		capricorn
Feb 19 - Mar 20	    water	pisces      	99%		85%		65%		90%		45%		70%		76%		capricorn
Aug 23 - Sep 22	    earth	virgo       	65%		99%		90%		65%		80%		65%		77%		capricorn
Jun 21 - Jul 22	    water	cancer      	99%		99%		70%		75%		70%		90%		84%		capricorn
Apr 20 - May 20	    earth	taurus      	85%		99%		85%		90%		90%		85%		89%		capricorn
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh aquarius
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Apr 20 - May 20	    earth	taurus      	15%		20%		10%		15%		1%		5%		11%		aquarius
Aug 23 - Sep 22	    earth	virgo       	1%		50%		40%		35%		30%		25%		30%		aquarius
Oct 23 - Nov 21	    water	scorpio     	40%		1%		50%		1%		30%		60%		30%		aquarius
Jun 21 - Jul 22	    water	cancer      	1%		35%		55%		50%		10%		25%		31%		aquarius
Dec 22 - Jan 19	    earth	capricorn   	5%		80%		65%		5%		40%		25%		37%		aquarius
Feb 19 - Mar 20	    water	pisces      	50%		50%		35%		1%		50%		40%		38%		aquarius
Mar 21 - Apr 19	    fire 	aries       	65%		85%		90%		40%		30%		99%		68%		aquarius
Sep 23 - Oct 22	    air  	libra       	90%		85%		40%		80%		50%		65%		68%		aquarius
Jan 20 - Feb 18	    air  	aquarius    	50%		99%		75%		40%		80%		99%		74%		aquarius
Nov 22 - Dec 21	    fire 	sagittarius 	80%		60%		99%		85%		90%		85%		83%		aquarius
May 21 - Jun 20	    air  	gemini      	85%		90%		99%		40%		95%		99%		85%		aquarius
Jul 23 - Aug 22	    fire 	leo         	99%		75%		90%		99%		80%		90%		89%		aquarius
--------------------------------------------------------------------------------------------------------------------------------------------------------------


./astro-compat.sh pisces
                                              Sexual &                      Communication                                      Shared         
     Dates         Element        Sign        Intimacy         Trust         & Intellect      Emotions         Values        Activities       Summary
--------------------------------------------------------------------------------------------------------------------------------------------------------------
May 21 - Jun 20	    air  	gemini      	15%		1%		20%		1%		5%		15%		10%		pisces
Jul 23 - Aug 22	    fire 	leo         	1%		1%		35%		15%		20%		10%		14%		pisces
Mar 21 - Apr 19	    fire 	aries       	20%		1%		70%		5%		35%		40%		29%		pisces
Sep 23 - Oct 22	    air  	libra       	50%		1%		5%		15%		60%		40%		29%		pisces
Jan 20 - Feb 18	    air  	aquarius    	50%		50%		35%		1%		50%		40%		38%		pisces
Nov 22 - Dec 21	    fire 	sagittarius 	30%		1%		85%		30%		65%		90%		50%		pisces
Jun 21 - Jul 22	    water	cancer      	85%		70%		85%		99%		25%		70%		72%		pisces
Feb 19 - Mar 20	    water	pisces      	75%		50%		60%		99%		80%		75%		73%		pisces
Dec 22 - Jan 19	    earth	capricorn   	99%		85%		65%		90%		45%		70%		76%		pisces
Oct 23 - Nov 21	    water	scorpio     	70%		65%		90%		99%		75%		85%		81%		pisces
Aug 23 - Sep 22	    earth	virgo       	99%		65%		85%		95%		75%		99%		86%		pisces
Apr 20 - May 20	    earth	taurus      	99%		80%		95%		99%		85%		70%		88%		pisces
--------------------------------------------------------------------------------------------------------------------------------------------------------------

```

