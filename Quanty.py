class Strategy:
    def __init__(self, strategy_name):
        self.strategy_type = strategy_name

    def __str__(self):
        return f"{self.strategy_name}"

    def __repr__(self):
        return f"{self.strategy_name}"
    
    def apply_strategy(self, data):
        # Void method to be implemented by child classes
        pass

class Momentum(Strategy):
    def apply_stategy(self, data):
        # Apply momentum strategy
        pass
    
class Backtest:
    def __init__(self, strategy, start_date, end_date, data):
        self.strategy = strategy
        self.start_date = start_date
        self.end_date = end_date
        self.data = data
        self.results = None

    def __str__(self):
        return f"{self.strategy}"

    def __repr__(self):
        return f"{self.strategy}"
    
    def run_backtest(self):
        # Run backtest
        pass

    def show_results(self):
        # Show backtest results
        pass

def Data_Handler(data, source):
    # Cleans data to the required format
    pass

#Example Data_Handler(fechamento.csv, "Economatica")