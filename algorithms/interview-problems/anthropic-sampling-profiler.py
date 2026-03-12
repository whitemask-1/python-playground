from dataclasses import dataclass
from typing import List

@dataclass
class Sample:
    ts: float
    stack: List[str]  # e.g. ["main"] or ["main", "my_fn"]

@dataclass
class Event:
    kind: str   # "start" or "end"
    ts: float
    name: str

def convert_to_trace(samples: List[Sample]) -> List[Event]:
    event_list = []
    previous_set = set()
    previous_set_stack = []
    for s in samples:
        current_set = set(s.stack)
        ended_processes = previous_set - current_set
        started_processes = current_set - previous_set
        event_list.extend(Event("end", s.ts, i) 
                          for i in sorted(ended_processes, key=lambda n: previous_set_stack.index(n), reverse=True)
                          )
        event_list.extend(Event("start", s.ts, i) 
                          for i in sorted(started_processes, key=lambda n: s.stack.index(n))
                          )
        previous_set = current_set
        previous_set_stack = s.stack

    return event_list

if __name__ == "__main__":
    s1 = Sample(7.5, ["main"])
    s2 = Sample(9.2, ["main", "my_fn"])
    s3 = Sample(10.7, ["main"])
    s4 = Sample(15.5, ["main", "my_fn", "my_fn2"])
    s5 = Sample(19.2, ["main", "my_fn"])

    samples = [s1, s2, s3, s4, s5]
    events = convert_to_trace(samples)

    for e in events:
        print(e.kind, e.ts, e.name)

