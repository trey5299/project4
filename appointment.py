class AbstractAppointment(object):
    pass


# public class Appointment extends AbstractAppointment
class Appointment(AbstractAppointment):

    file = open("Appointments.txt")

    # StringBuilder sb = new StringBuilder
    sb = ""

    # Constructor
    def __init__(self, owner, description, beginTime, beginDate, endDate, endTime):

        """CONNVERTING THE BEWLOW LINES
        self.owner = owner
        self.description = description
        self.beginTime = beginTime
        self.beginDate = beginDate
        self.endTime = endTime
        self.endTime = endTime
        """

        self.owner = owner
        self.description = description
        self.beginTime = beginTime
        self.beginDate = beginDate
        self.endTime = endTime
        self.endTime = endTime

        # public void String (String owner) {
        def getOwner(self):
            # this.owner= owner+sb.append("+);
            return self.owner + self.sb + "+"


        def getDescription(self):

            return self.description + self.sb + "+"