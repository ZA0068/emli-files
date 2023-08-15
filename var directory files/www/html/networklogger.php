<?php
$log_file = '/home/EMLI_TEAM_24/log/networklogging.log';

if (!file_exists($log_file)) {
    die("Error: Log file '$log_file' does not exist.");
}

if (!is_readable($log_file)) {
    die("Error: Log file '$log_file' is not readable.");
}

$log = file($log_file);

if ($log === false) {
    die("Error: Failed to read log file '$log_file'.");
}

$log = array_slice($log, -6);

$data = array();

function formatBytes($bytes) {
    $units = array('Bytes', 'KB', 'MB', 'GB', 'TB');
    $bytes = max($bytes, 0);
    $pow = floor(($bytes ? log($bytes) : 0) / log(1024));
    $pow = min($pow, count($units) - 1);
    $bytes /= pow(1024, $pow);
    return round($bytes, 2) . ' ' . $units[$pow];
}

foreach ($log as $line) {
    $parts = explode(':', $line, 2);
    if (count($parts) == 2) {
        $key = trim($parts[0]);
        $value = trim($parts[1]);

        if ($key == 'Is internet connected') {
            $value = ($value == '1') ? 'Yes' : 'No';
        } else if (strpos($key, 'data') !== false) { // If it's a data field
            $value = formatBytes($value);
        }

        $data[$key] = $value;
    }
}

echo '<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

tr:nth-child(even){background-color: #e6e6ff}

th {
  background-color: #20A4F0;
  color: white;
}
</style>';

echo '<table>';
foreach ($data as $key => $value) {
    echo '<tr>';
    echo '<th>' . htmlspecialchars($key) . '</th>';
    echo '<td>' . htmlspecialchars($value) . '</td>';
    echo '</tr>';
}
echo '</table>';
?>