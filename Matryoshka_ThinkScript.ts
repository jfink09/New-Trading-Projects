def Intradaylow = low;
def Intradayhigh = high;

def matrix = if (high[2] >= high[1] and low[2] <= low[1]) and (high[1] >= high[0] and low[1] <= low[0]) then 1 else 0;

plot signal = matrix within 1 bars;

signal.SetDefaultColor(Color.WHITE);
signal.SetPaintingStrategy(PaintingStrategy.BOOLEAN_ARROW_UP);
