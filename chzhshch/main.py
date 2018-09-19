import sys
import datetime

from external_package import tushare_helper as th
from inner_package import standardized as standard
from inner_package import show

# original = th.TushareHelper('000001', datetime.date.today()+ datetime.timedelta(days=-1),datetime.date.today() + datetime.timedelta(days=+1),'1min')
# original = th.TushareHelper('000001', '2017-12-04', '2018-12-12', 'D')
# original = th.TushareHelper('600756', '2018-01-01', '2018-12-31', 'D', [5,20],'E')
original = th.TushareHelper('600756', '2018-08-01', '2018-12-31', '60MIN', [5,20],'E')

original.data_transfer()
sta = standard.StandardHandle(original.data_original)
sta.deal_candle()
sta.get_top_bottom()

date_tickers = sta.date_tickers
my_plot = show.PlotShow(date_tickers, '600756')
# my_plot.candle_show(sta.standardized_list_ex, [])
# my_plot.candle_show(sta.standardized_list_ex, sta.top_bottom_list_ex)
my_plot.candle_show(sta.standardized_list_ex,
                    sta.standardized_top_bottom_list_ex)