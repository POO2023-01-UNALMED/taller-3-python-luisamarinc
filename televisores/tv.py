class TV:

	_numTV=0

	def __init__(self, marca, estado):
		self._marca= marca
		self._estado = estado
		self._canal =1
		self._precio = 500
		self._volumen = 1
		self._control = None
		TV._numTV+=1

	def getMarca(self):
		return self._marca

	def setMarca(self, marca):
		self._marca = marca

	def getMarca(self):
		return self._canal

	def setCanal(self, canal):
		if self._estado:
			if  0 < canal < 121:
				self._canal =  canal


	def getPrecio(self):
		return self._precio

	def setPrecio(self, precio):
		self._precio = precio

	def getVolumen(self):
		return self._volumen

	def setVolumen(self, volumen):
		if self._estado: 
			self._volumen = volumen
		
	@classmethod
	def getNumTV(cls):
		return cls._numTV

	@classmethod
	def setNumTV(cls, numTv):
		cls._numTV = numTv

	def getControl(self):
		return self._control
	
	def setControl(self, control):
		self._control = control

	def turnOn(self):
		self._estado = True
	
	def turnOn(self):
		self._estado = False

	def getEstado(self):
		return self._estado
	

	def canalUp(self):
		if self._estado:
			if 0 < self._canal <= 119:
				self._canal +=1 

	def canalDown(self):
		if self._estado:
			if 1 < self._canal <= 120:
				self._canal -=1 

	
	def volumenUp(self):
		if self._estado:
			if -1 < self._volumen <= 6:
				self._volumen +=1 



	def volumenDown(self):
		if self._estado:
			if 0 < self._volumen <= 7:
				self._volumen +=1 

	