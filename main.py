from AlgorithmImports import *


# Use 5 ETFs (SPY - US stocks, EFA - foreign stocks, IEF - bonds, VNQ - REITs,
# GSG - commodities), equal weight the portfolio. Hold asset class ETF only when
# it is over its 10 month Simple Moving Average, otherwise stay in cash.

class AssetClassTrendFollowing(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 1, 1)
        self.SetCash(100000)

        self.data = {}
        period = 5 * 21
        self.SetWarmUp(period)

        self.symbols = ["SPY", "EFA", "IEF", "VNQ", "GSC"]
        self.rebalance_flag = False

        self.tracked_symbol = None
        for symbol in self.symbols:
            self.AddEquity(symbol, Resolution.Daily)
            self.data[symbol] = self.SMA(symbol, period, Resolution.Daily)

        self.data["SPY"].Updated += self.OnSmaUpdated
        self.recent_month = -1
        self.SetBenchmark("SPY")

   # def OnSmaUpdated(self, sender, updated):
   #     # set rebalance flag
   #     if self.recent_month != self.Time.month:
   #         self.recent_month = self.Time.month
   #         self.rebalance_flag = True

    def OnSmaUpdated(self, sender, updated):
        # set rebalance flag
        if self.recent_month != self.Time.month:
            self.recent_month = self.Time.month
            self.rebalance_flag = True

    def OnData(self, data):
        # rebalance once a month
        if self.rebalance_flag:
            self.rebalance_flag = False

            long = []
            for symbol in self.symbols:
                if symbol in data and data[symbol]:
                    if self.data[symbol].IsReady:
                        if data[symbol].Value > self.data[symbol].Current.Value:
                            long.append(symbol)

            # Trade execution.
            invested = [x.Key.Value for x in self.Portfolio if x.Value.Invested]
            for symbol in invested:
                if symbol not in long:
                    self.Liquidate(symbol)

            for symbol in long:
                hist = self.History(self.Symbol(symbol), 2, Resolution.Daily)
                self.SetHoldings(symbol, 1 / len(long))

