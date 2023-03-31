from data_visualization import DataVisualisation
import configparser



if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('config.ini')


    myobj = DataVisualisation(config.get('database', 'host'),
                              config.get('database', 'database'), 
                              config.get('database', 'username'), 
                              config.get('database', 'password'))

    myobj.datavisualization()


