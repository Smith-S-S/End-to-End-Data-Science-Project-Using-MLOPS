import os
from mlproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlproject.entity.config_entity import DataTransformationConfig
from sklearn.preprocessing import LabelEncoder


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def label_encode_column(self, df):
        label_encoder = LabelEncoder()
        df['PType'] = label_encoder.fit_transform(df['Type'])
        logger.info("Label encoded for column: Type")
        df = df.drop(['UDI', 'Type', 'Product ID'], axis=1)
        logger.info("Dropped columns: UDI, Type, Product ID")
        
        return df

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Label encode the column
        data = self.label_encode_column(data)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

        