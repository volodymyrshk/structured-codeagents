import io
import sys

class PythonExecutor:
    def execute(self, code: str, debug: bool = False):
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output
        
        try:
            exec(code)
            return redirected_output.getvalue()
        except Exception as e:
            if debug:
                import traceback
                return f"Execution Error: {e}\n{traceback.format_exc()}"
            else:
                return f"Execution Error: {e}"
        finally:
            sys.stdout = old_stdout
