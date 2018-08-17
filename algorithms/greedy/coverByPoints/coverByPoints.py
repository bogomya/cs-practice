def coverByPoints(segments: (int, int)):
    points = []
    orderedSegments = sorted(segments, key=lambda segment: segment[1])
    for i, segment in enumerate(orderedSegments):
        lastPoint = points[-1] if points else 0
        isLastSegment = i == len(orderedSegments) - 1
        if isLastSegment and lastPoint > segment[0]:
            continue

        if segment[1] > lastPoint:
            points.append(segment[1])

    return points


def main():
    segments = []
    n = int(input())
    for i in range(n):
        begin, end = map(lambda i: int(i), input().split(" "))
        segments.append(( begin, end))
    points = coverByPoints(segments)
    print(" ".join(points))

if __name__ == "__main__":
    main()
