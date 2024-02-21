class BaseSubstrate:

    def make_nodes(self, query_res):
        raise NotImplementedError

    def make_conn(self, query_res):
        raise NotImplementedError

    @property
    def query_coors(self):
        raise NotImplementedError

    @property
    def num_inputs(self):
        raise NotImplementedError

    @property
    def num_outputs(self):
        raise NotImplementedError

    @property
    def nodes_cnt(self):
        raise NotImplementedError

    @property
    def conns_cnt(self):
        raise NotImplementedError
