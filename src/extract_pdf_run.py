import asyncio
import pymupdf4llm

from pipelex import pretty_print
from pipelex.core.stuff_content import ListContent, TextContent
from pipelex.core.stuff_factory import StuffFactory
from pipelex.core.working_memory_factory import WorkingMemoryFactory
from pipelex.hub import get_report_delegate
from pipelex.pipelex import Pipelex
from pipelex.run import run_pipe_code


async def process_capital_increase_report(path_to_pdf: str):
    # first step : Convert the pdf to text using llammaparse (or pymupdf)
    md_text = pymupdf4llm.to_markdown(path_to_pdf)  # type: ignore

    # second step : run the pipe
    working_memory = WorkingMemoryFactory.make_from_text(text=md_text, name="operation_note_text")

    pipe_output = await run_pipe_code(
        pipe_code="extract_pdf_capital_increase_sequence",
        working_memory=working_memory,
    )

    pretty_print(pipe_output, title="Processing output for invoice")
    get_report_delegate().general_report()


pdf_path = "data/financial_reports/20240527_Capital_Increase_Securities_Note_FR_0.pdf"
Pipelex.make()
asyncio.run(process_capital_increase_report(pdf_path))
