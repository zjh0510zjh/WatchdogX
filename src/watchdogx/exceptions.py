"""Custom exceptions"""
class WatchdogXError(Exception): pass
class AgentExecutionError(WatchdogXError): pass
class ConfigurationError(WatchdogXError): pass
class MemoryStoreError(WatchdogXError): pass
