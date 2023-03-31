from data_transformation import DataTransformation
import matplotlib.pyplot as plt

class DataVisualisation(DataTransformation):

    def __init__(self, hostname, database, user, password):
        """Visualize the data

        Args:
            hostname (string): host ames
            database (string): database
            user (string): username
            password (string): password
        """
        super().__init__(hostname, database, user, password)
        
    def datavisualization(self):
        """Method to visualize the data
        """
        df_visualize = self.trasform_data_os()
        df_visualize.plot()
        plt.show()



