class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool =  False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
        """
        Declares all the instance variables 
        status = declares the power of the tv
        muted = declares the muted or unmuted 
        volume = declares the volume of the tv
        channel declares the channel the tv is on
        """




    def power(self) -> None:
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False
        """
        Turns the tv on or off
        sets the status to true or false
        """



    def mute(self) -> None:
        if self.__status == False:
            pass
        elif self.__muted == False:
            self.__muted = True
        elif self.__muted == True:
            self.__muted = False
        """
        Mutes or unmutes the tv
        set the muted to true or false
        """

    def channel_up(self) -> None:
        if self.__status == False:
            pass
        elif self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1
        """
        When the TV is on, it increases the channel and 
        when it goes over the max it is set back to the min
        :param status is checked for true or false
        :param channel is set to min if at max or is added by 1
        """
    def channel_down(self) -> None:
        if self.__status == False:
            pass
        elif self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1
        """
        When the TV is on, it decreases the channel and 
        when it goes under the min it is set back to the max
        :param status is checked for true or false
        :param channel is set to max if at min or subtracted by one
        """


    def volume_up(self) -> None:
        if self.__status == False:
            pass
        elif self.__muted == True:
            self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME
            else:
                self.__volume += 1
        elif self.__volume == self.MAX_VOLUME:
            self.__volume = self.MAX_VOLUME
        else:
            self.__volume += 1
        """
        When the TV is on, the TV becomes unmuted and the volume 
        increases by one
        :param status checks true or false
        :param muted unmutes the tv if it is muted
        :param volume checks if it is at max volume and keeps it there
        and also adds 1 to the volume
        """

    def volume_down(self) -> None:
        if self.__status == False:
            pass
        elif self.__muted == True:
            self.__muted = False
            if self.__volume == self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume -= 1
        elif self.__volume == self.MIN_VOLUME:
            self.__volume = self.MIN_VOLUME
        else:
            self.__volume -= 1
    """
    When the TV is on, the volume is decreased by 1 and the tv is unmuted
    :param status checks true or false
    :param muted unmutes the tv
    :param volume decreases by 1 or keeps it at the min volume
    """

    def __str__(self) -> str:
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME},'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume},'

    """
    Returns the power, channel, and volume every iteration 
    :return status, channel, volume 
    """


