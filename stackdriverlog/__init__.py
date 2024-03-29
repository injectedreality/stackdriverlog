# -*- coding: utf-8 -*-
import structlog

def init_stack_driver_logging():
    structlog.configure_once(processors=[structlog.processors.format_exc_info,
                                         structlog.processors.JSONRenderer()],
                             context_class=dict,
                             )

def get_logger():
    return structlog.get_logger()