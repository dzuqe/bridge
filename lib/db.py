class Db:
    def __init__(self):
        self.from_addr = ''
        self.to_addr = ''
        self.value = ''
        self.from_tx = ''
        self.to_tx = ''
        self.status = ''
        self.id = -1

    def start_with_id(self, id):
        data = db.exec(f"select * from bridge.algo_matic where id = {id}")
        print(data)
        self.from_addr = data.from
        self.to_addr = data.to
        self.value = data.value
        self.from_tx = data.from_tx
        self.to_tx = data.to_tx
        self.status = data.status
        self.id = id

    def start_with_data(self, from, to, value):
        self.from_addr = from
        self.to_addr = to
        self.value = value
        self.from_tx = ''
        self.to_tx = ''
        self.status = ''
        self.id = -1


    def create(self):
        self.status = 'PENDING'
        self.id = db.exec('insert into bridge.algo_matic (from, to, value, status) values (from, to, value, PENDING')

   
    def update(self):
        db.exec(f"update bridge.algo_matic where id = {self.id}")


