import tensorflow as tf
from tensorflow.contrib.keras.python.keras.layers import Conv3D, MaxPooling3D, UpSampling3D, Activation, Conv3DTranspose
from tf_layers import *


def BraTS2ScaleDenseNetConcat(input):

    x = Conv3D(filters=24, kernel_size=3, strides=1, padding='same')(input)
    x = DenseNetUnit3D(x, growth_rate=12, ksize=3, rep=6)

    out_15rf = BatchNormalization(center=True, scale=True)(x)
    out_15rf = Activation('relu')(out_15rf)
    out_15rf = Conv3DWithBN(out_15rf, filters=96, ksize=1, strides=1, name='out_15_postconv')

    x = DenseNetUnit3D(x, growth_rate=12, ksize=3, rep=6)

    out_27rf = BatchNormalization(center=True, scale=True)(x)
    out_27rf = Activation('relu')(out_27rf)
    out_27rf = Conv3DWithBN(out_27rf, filters=168, ksize=1, strides=1, name='out_27_postconv')

    return out_15rf, out_27rf


def BraTS2ScaleDenseNet(input, num_labels):

    x = Conv3D(filters=24, kernel_size=3, strides=1, padding='same')(input)
    x = DenseNetUnit3D(x, growth_rate=12, ksize=3, rep=6)

    out_15rf = BatchNormalization(center=True, scale=True)(x)
    out_15rf = Activation('relu')(out_15rf)
    out_15rf = Conv3DWithBN(out_15rf, filters=96, ksize=1, strides=1, name='out_15_postconv')

    x = DenseNetUnit3D(x, growth_rate=12, ksize=3, rep=6)

    out_27rf = BatchNormalization(center=True, scale=True)(x)
    out_27rf = Activation('relu')(out_27rf)
    out_27rf = Conv3DWithBN(out_27rf, filters=168, ksize=1, strides=1, name='out_27_postconv')

    score_15rf = Conv3D(num_labels, kernel_size=1, strides=1, padding='same')(out_15rf)
    score_27rf = Conv3D(num_labels, kernel_size=1, strides=1, padding='same')(out_27rf)

    score = score_15rf[:, 13:25, 13:25, 13:25, :] + \
            score_27rf[:, 13:25, 13:25, 13:25, :]

    return score


def BraTS3ScaleDenseNet(input, num_labels):

    x = Conv3D(filters=24, kernel_size=3, strides=1, padding='same')(input)
    x = DenseNetUnit3D(x, growth_rate=12, ksize=3, rep=5)

    out_13rf = BatchNormalization(center=True, scale=True)(x)
    out_13rf = Activation('relu')(out_13rf)
    out_13rf = Conv3DWithBN(out_13rf, filters=84, ksize=1, strides=1, name='out_13_postconv')

    x = DenseNetUnit3D(x, growth_rate=12, ksize=3, rep=5)

    out_23rf = BatchNormalization(center=True, scale=True)(x)
    out_23rf = Activation('relu')(out_23rf)
    out_23rf = Conv3DWithBN(out_23rf, filters=144, ksize=1, strides=1, name='out_23_postconv')

    x = DenseNetUnit3D(x, growth_rate=12, ksize=3, rep=5)

    out_33rf = BatchNormalization(center=True, scale=True)(x)
    out_33rf = Activation('relu')(out_33rf)
    out_33rf = Conv3DWithBN(out_33rf, filters=204, ksize=1, strides=1, name='out_33_postconv')

    score_13rf = Conv3D(num_labels, kernel_size=1, strides=1, padding='same')(out_13rf)
    score_23rf = Conv3D(num_labels, kernel_size=1, strides=1, padding='same')(out_23rf)
    score_33rf = Conv3D(num_labels, kernel_size=1, strides=1, padding='same')(out_33rf)

    score = score_13rf[:, 16:28, 16:28, 16:28, :] + \
            score_23rf[:, 16:28, 16:28, 16:28, :] + \
            score_33rf[:, 16:28, 16:28, 16:28, :]

    return score



def BraTS1ScaleDenseNet(input, num_labels):

    x = Conv3D(filters=36, kernel_size=5, strides=1, padding='same')(input)
    x = DenseNetUnit3D(x, growth_rate=18, ksize=3, rep=6)

    out_15rf = BatchNormalization(center=True, scale=True)(x)
    out_15rf = Activation('relu')(out_15rf)
    out_15rf = Conv3DWithBN(out_15rf, filters=144, ksize=1, strides=1, name='out_17_postconv1')
    out_15rf = Conv3DWithBN(out_15rf, filters=144, ksize=1, strides=1, name='out_17_postconv2')

    score_15rf = Conv3D(num_labels, kernel_size=1, strides=1, padding='same')(out_15rf)

    score = score_15rf[:, 8:20, 8:20, 8:20, :]
    return score