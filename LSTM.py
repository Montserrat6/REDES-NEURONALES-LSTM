from keras.models import Sequential
from keras.layers import LSTM, Dense

# Definir el modelo de la LSTM
model = Sequential()
model.add(LSTM(64, input_shape=(timesteps, input_dim)))
model.add(Dense(num_classes, activation='softmax'))

# Compilar el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, batch_size=32, epochs=10, validation_data=(X_test, y_test))
