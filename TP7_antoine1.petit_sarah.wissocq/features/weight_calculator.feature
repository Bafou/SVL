Feature: Weight calculator

	Formula
    For a man : height x 100 - 100 - (height x 100 - 150) / 4
    For a woman : height x 100 - 100 - (height x 100 - 150) / 2.5

Scenario Outline: temperature computations
	Given height and gender and the ideal weight
	Then with <height> meter and <gender> I obtain a ideal weight <weight> kg

Examples: temperature values
| height | weight | gender |
| 1.90	 | 80.0   | man    |
| 1.60	 | 57.5   | man    |
| 1.50	 | 50.0   | woman  |
| 2.0	 | 80.0   | woman  |