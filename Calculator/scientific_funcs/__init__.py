from .cos_call import cos_
from .exp_call import exponential
from .log_call import log_
from .relu_call import relu_
from .sigmoid_call import sigmoid_
from .sin_call import sin_
from .softmax_call import softmax_
from .tan_call import tan_,tan_h


# __all__ = (sin_call.__all__ + sigmoid_call.__all__ + log_call.__all__ + relu_call.__all__ + exp_call.__all__ +
#            sigmoid_call.__all__ + tan_call.__all__ + cos_call.__all__)

__all__ = ('cos_','exponential','log_','relu_','sigmoid_','sin_','softmax_','tan_h','tan_')
