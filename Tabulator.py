

class Tabulator:

    def get_as_table(self, parsed_data):
        table = []
        all_time_centers = []

        # First pass: collect all time centers and create initial table rows
        for line in parsed_data:
            row = ['', '']  # Initialize with empty surname and firstname
            times = []
            for word in line['words']:
                if word['type'] == 'surname':
                    row[0] = word['text']
                elif word['type'] == 'firstname':
                    row[1] = word['text']
                elif word['type'] == 'time':
                    center = (word['bbox'][0] + word['bbox'][2]) / 2
                    times.append((center, word['text']))
                    all_time_centers.append(center)
            
            table.append((row, times))

        # Cluster time centers
        if all_time_centers:
            clusters = self.cluster_1d(all_time_centers)
            num_clusters = len(clusters)

            # Second pass: fill in the times based on clusters
            for i, (row, times) in enumerate(table):
                full_row = row + [''] * num_clusters
                for center, time in times:
                    cluster_index = next(i for i, cluster in enumerate(clusters) if cluster[0] <= center <= cluster[1])
                    full_row[2 + cluster_index] = time
                table[i] = full_row

        return table

    def cluster_1d(self, points, threshold=100):
        points = sorted(points)
        clusters = []
        current_cluster = [points[0]]

        for point in points[1:]:
            if point - current_cluster[-1] > threshold:
                clusters.append((min(current_cluster), max(current_cluster)))
                current_cluster = [point]
            else:
                current_cluster.append(point)

        clusters.append((min(current_cluster), max(current_cluster)))
        return clusters
