import pysynth  as ps 
tempo=1
test=(
('a',4+tempo),('a',4+tempo),('a',4+tempo),
('c',4+tempo),('c',4+tempo),
('b',8+tempo),('a',8+tempo),('g',8+tempo),
('r',8+tempo),
('c',4+tempo),('c',4+tempo),
('b',8+tempo),('a',8+tempo),('g',4+tempo),
('r',4+tempo),
('a',4+tempo),('g',4+tempo),('f',4+tempo),('g',2+tempo),('a',2+tempo),
('r',4+tempo),
('a',4+tempo),('g',4+tempo),('f',4+tempo),
('d',2+tempo),('d',2+tempo),
('r',6+tempo),
('f',4+tempo),('e',4+tempo),('f',4+tempo),('e',2+tempo),
('f',4+tempo),('g',4+tempo),
('r',6+tempo),
('f',4+tempo),('e',4+tempo),('f',4+tempo),('g',4+tempo),
('f',4+tempo),('e',4+tempo),('d',4+tempo),
('r',4+tempo),
('f',4+tempo),('e',4+tempo),('f',4+tempo),('e',2+tempo),
('f',4+tempo),('g',4+tempo),
('r',6+tempo),
('f',4+tempo),('e',4+tempo),('f',4+tempo),('g',4+tempo),
('f',4+tempo),('e',4+tempo),('d',4+tempo)
)
ps.make_wav(test,fn="Test4.wave")