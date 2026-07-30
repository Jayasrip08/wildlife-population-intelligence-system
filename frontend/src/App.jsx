import React, { useState } from 'react';
import './App.css';

// ======================
// SVG Icons (Lucide-style)
// ======================
const GearIcon = (props) => (<svg width={props.width || "20"} height={props.height || "20"} fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 010-2.83 2 2 0 012.83 0l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 0 2 2 0 010 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z"></path></svg>);
const LeafIcon = () => (<svg width="24" height="24" fill="none" stroke="var(--primary)" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><path d="M11 20A7 7 0 019.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"></path><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"></path></svg>);
const GridMenuIcon = () => (<svg width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>);

// Sidebar Module Icons
const SvgDashboard = () => <svg width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="9"></rect><rect x="14" y="3" width="7" height="5"></rect><rect x="14" y="12" width="7" height="9"></rect><rect x="3" y="16" width="7" height="5"></rect></svg>;
const SvgUsers = () => <svg width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 00-3-3.87"></path><path d="M16 3.13a4 4 0 010 7.75"></path></svg>;
const SvgCamera = () => <svg width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><path d="M23 19a2 2 0 01-2 2H3a2 2 0 01-2-2V8a2 2 0 012-2h4l2-3h6l2 3h4a2 2 0 012 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>;
const SvgMap = () => <svg width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg>;
const SvgFile = () => <svg width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>;
const SvgAlert = () => <svg width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>;
const SvgMusic = () => <svg width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>;

const getIconForLabel = (label) => {
  if (label === 'Dashboard') return <SvgDashboard />;
  if (label === 'User Management' || label === 'Field Teams') return <SvgUsers />;
  if (label === 'Camera Traps' || label === 'Species Analysis') return <SvgCamera />;
  if (label === 'GIS Mapping' || label === 'Patrol Zones' || label === 'Protected Zones' || label === 'Tracked Animals' || label === 'Corridors') return <SvgMap />;
  if (label === 'Alerts' || label === 'Fire Risk' || label === 'Incidents') return <SvgAlert />;
  if (label === 'Bioacoustics' || label === 'Audio Lab') return <SvgMusic />;
  if (label === 'Settings') return <GearIcon width="18" height="18" />;
  return <SvgFile />; // Reports, Datasets
}

// ======================
// App Data & Config
// ======================

const initialUsers = [
  { username: 'admin', password: 'root', role: 'admin', name: 'System Administrator' },
  { username: 'researcher', password: 'root', role: 'researcher', name: 'Dr. Priya Sharma' },
  { username: 'officer', password: 'root', role: 'conservation_officer', name: 'Officer Rajan Mehra' },
  { username: 'forest', password: 'root', role: 'forest_department', name: 'Forest Warden Singh' },
];

const ROLE_LABELS = {
  admin: 'Administrator',
  researcher: 'Researcher',
  conservation_officer: 'Conservation Officer',
  forest_department: 'Forest Department',
};

const NAV_ITEMS = {
  admin: ['Dashboard', 'Camera Traps', 'Bioacoustics', 'GIS Mapping', 'User Management', 'Settings'],
  researcher: ['Dashboard', 'Datasets', 'Species Analysis', 'Audio Lab', 'Reports', 'Settings'],
  conservation_officer: ['Dashboard', 'Alerts', 'Field Teams', 'Tracked Animals', 'Protected Zones', 'Settings'],
  forest_department: ['Dashboard', 'Patrol Zones', 'Corridors', 'Fire Risk', 'Incidents', 'Settings'],
};

// ======================
// Shared UI Components
// ======================

function TopNavbar({ user }) {
  return (
    <header className="navbar">
      <div className="navbar-brand">
        <LeafIcon />
        <div>
          <div className="brand-name">Wildlife OS</div>
          <div className="brand-sub">Intelligence System</div>
        </div>
      </div>
      <div className="navbar-center">
        <input type="text" placeholder="Search species, datasets, locations..." />
      </div>
      <div className="navbar-right">
        {/* Settings and Notification buttons removed; Settings is now exclusively in the sidebar. */}
        <div className="nav-user" style={{ borderLeft: 'none', paddingLeft: 0 }}>
          <div className="nav-avatar">{user.name.charAt(0)}</div>
          <span>{user.name.split(' ')[0]}</span>
        </div>
      </div>
    </header>
  );
}

function Sidebar({ user, onLogout, activeTab, setActiveTab }) {
  return (
    <aside className="sidebar">
      <div className="sidebar-section-label" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <GridMenuIcon /> MAIN MENU
      </div>
      {NAV_ITEMS[user.role].map((label) => (
        <a 
          href="#" 
          key={label} 
          onClick={(e) => { e.preventDefault(); setActiveTab(label); }}
          className={`nav-item ${activeTab === label ? 'active' : ''}`}
        >
          <span className="nav-icon">{getIconForLabel(label)}</span>
          <span>{label}</span>
        </a>
      ))}
      
      <div className="sidebar-bottom">
        <div className="sidebar-divider"></div>
        <button className="logout-btn" onClick={onLogout}>Sign Out</button>
      </div>
    </aside>
  );
}

function StatCard({ icon, color, label, value, trend, trendType }) {
  return (
    <div className="stat-card">
      <div className={`stat-icon-box c-${color}`}>
        {typeof icon === 'string' ? <span style={{fontSize: '1.4rem'}}>{icon}</span> : icon}
      </div>
      <div className="stat-body">
        <div className="stat-label">{label}</div>
        <div className="stat-value">{value}</div>
        <div className={`stat-trend t-${trendType}`}>{trend}</div>
      </div>
    </div>
  );
}

function DetectionList() {
  const items = [
    { time: '10m ago', species: 'Panthera leo', conf: '98%', type: 'Image' },
    { time: '1h ago', species: 'Loxodonta africana', conf: '95%', type: 'Image' },
    { time: '3h ago', species: 'Turdus merula', conf: '89%', type: 'Audio' },
    { time: '5h ago', species: 'Panthera pardus', conf: '91%', type: 'Image' },
  ];
  return (
    <ul className="detection-list">
      {items.map((d, i) => (
        <li key={i} className="det-item">
          <div className="det-top">
            <span className="det-species">{d.species}</span>
            <span className={`det-type ${d.type === 'Audio' ? 'audio' : ''}`}>{d.type}</span>
          </div>
          <div className="det-bottom">
            <span className="det-time">{d.time}</span>
            <span className="det-conf">{d.conf} match</span>
          </div>
        </li>
      ))}
    </ul>
  );
}

function GenericScreen({ title }) {
  return (
    <div className="scroll-area">
      <div className="page-header">
        <h1 className="page-title">{title}</h1>
        <p className="page-subtitle">Module initialized. Live data streaming will begin upon server connect.</p>
      </div>
      
      {title.includes('Map') || title.includes('Zone') || title.includes('Corridors') || title.includes('Animals') ? (
        <div className="card" style={{ height: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#f1f5f9', border: '1px dashed #cbd5e1' }}>
          <div style={{ textAlign: 'center', color: '#64748b' }}>
            <div style={{ marginBottom: '1rem', color: '#94a3b8' }}><SvgMap /></div>
            <h3 style={{color: '#334155', marginBottom: '0.5rem'}}>Geospatial Intel Loading...</h3>
            <p style={{fontSize: '0.9rem', maxWidth: '320px', margin: '0 auto'}}>Satellite telemetry and ground sensor spatial data is currently synchronizing with the global tracking network.</p>
          </div>
        </div>
      ) : title.includes('Camera') || title.includes('Analysis') ? (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
          {[1,2,3,4].map(i => (
            <div key={i} className="card" style={{ height: '220px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', background: '#f8fafc', border: '1px dashed #cbd5e1' }}>
              <div style={{color: '#94a3b8'}}><SvgCamera /></div>
              <div style={{ marginTop: '0.75rem', fontWeight: '600', color: '#334155' }}>Feed 0{i} - Sector {['Alpha', 'Bravo', 'Charlie', 'Delta'][i-1]}</div>
              <div style={{ fontSize: '0.8rem', color: '#10b981', marginTop: '0.25rem', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                <span style={{display: 'inline-block', width: '8px', height: '8px', background: '#10b981', borderRadius: '50%'}}></span>
                Live - Scanning...
              </div>
            </div>
          ))}
        </div>
      ) : title.includes('Audio') || title.includes('Bioacoustics') ? (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          {[1,2,3].map(i => (
            <div key={i} className="card" style={{ display: 'flex', alignItems: 'center', gap: '1.25rem', padding: '1.25rem' }}>
              <div style={{background: '#e0f2fe', padding: '1.25rem', borderRadius: '8px', color: '#0284c7'}}><SvgMusic/></div>
              <div style={{flex: 1}}>
                 <h4 style={{margin: '0 0 0.3rem', color: '#0f172a'}}>Acoustic Sensor Node {i * 42}</h4>
                 <p style={{margin: 0, fontSize: '0.85rem', color: '#64748b'}}>Pattern match: {i === 1 ? 'Loxodonta africana (94%)' : 'Panthera leo (88%)'}</p>
                 <div style={{height: '4px', width: '100%', background: '#e2e8f0', borderRadius: '2px', marginTop: '0.75rem'}}>
                    <div style={{height: '100%', width: i === 1 ? '94%' : '88%', background: '#0284c7', borderRadius: '2px'}}></div>
                 </div>
              </div>
              <button className="btn-outline">Analyze Waveform</button>
            </div>
          ))}
        </div>
      ) : (
        <div className="card">
          <div className="card-header">
            <h3>Module Records</h3>
            <button className="btn-outline">Export CSV</button>
          </div>
          <table className="data-table">
            <thead><tr><th>Record ID</th><th>Timestamp</th><th>Source</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td>DOC-8821</td><td>Today, 10:45 AM</td><td>Field Upload (JSON)</td><td><span className="role-badge rb-researcher">Processed</span></td></tr>
              <tr><td>SND-4492</td><td>Today, 11:30 AM</td><td>Acoustic Node 12</td><td><span className="role-badge rb-researcher">Processed</span></td></tr>
              <tr><td>IMG-1104</td><td>Today, 12:15 PM</td><td>Camera Trap B</td><td><span className="role-badge rb-admin">Queued</span></td></tr>
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

function SettingsPage() {
  return (
    <div className="scroll-area">
      <div className="page-header">
        <h1 className="page-title">System Settings</h1>
        <p className="page-subtitle">Configure application preferences and system parameters.</p>
      </div>
      <div className="card">
        <div className="card-header">
          <h3>General Preferences</h3>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', color: 'var(--text-md)' }}>
          <label style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', cursor: 'pointer' }}>
            <input type="checkbox" defaultChecked style={{width: '16px', height: '16px'}} /> Enable Dark Mode Detection (Auto)
          </label>
          <label style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', cursor: 'pointer' }}>
            <input type="checkbox" defaultChecked style={{width: '16px', height: '16px'}} /> Sync Offline Data Automatically
          </label>
          <label style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', cursor: 'pointer' }}>
            <input type="checkbox" defaultChecked style={{width: '16px', height: '16px'}} /> Compact Data Tables
          </label>
          <p style={{ marginTop: '1.5rem', fontSize: '0.85rem', color: 'var(--text-lt)' }}>Advanced settings integration will be available in the next backend update.</p>
        </div>
      </div>
    </div>
  );
}

function AlertsPage() {
  return (
    <div className="scroll-area">
      <div className="page-header">
        <h1 className="page-title">Threat Alerts & Notifications</h1>
        <p className="page-subtitle">Monitor and respond to critical situations in the field.</p>
      </div>
      <div className="card">
        <div className="card-header"><h3>Active Alerts Log</h3></div>
        <ul className="alert-list">
          <li className="alert-item high">
            <span className="al-level">HIGH</span>
            <span className="al-text">Poaching activity detected — Sector 7B, Serengeti</span>
            <span className="al-time">12 min ago</span>
          </li>
          <li className="alert-item med">
            <span className="al-level">MED</span>
            <span className="al-text">Unusual lion movement — Near reserve boundary</span>
            <span className="al-time">1 hr ago</span>
          </li>
          <li className="alert-item low">
            <span className="al-level">LOW</span>
            <span className="al-text">Camera trap offline — Node #14</span>
            <span className="al-time">3 hrs ago</span>
          </li>
        </ul>
      </div>
    </div>
  );
}

// ======================
// Role Dashboards
// ======================

function AdminDashboard({ user, users, setUsers, onLogout }) {
  const [activeTab, setActiveTab] = useState('Dashboard');
  const [showAdd, setShowAdd] = useState(false);
  const [nu, setNu] = useState({ username: '', password: '', role: 'researcher', name: '' });
  const [msg, setMsg] = useState('');

  const handleAdd = (e) => {
    e.preventDefault();
    if (users.find(u => u.username === nu.username)) { setMsg('Username already exists!'); return; }
    setUsers([...users, nu]);
    setMsg('User created successfully!');
    setNu({ username: '', password: '', role: 'researcher', name: '' });
  };

  const renderContent = () => {
    if (activeTab === 'Settings') return <SettingsPage />;
    if (activeTab === 'Alerts') return <AlertsPage />;
    
    if (activeTab === 'User Management') return (
      <div className="scroll-area">
        <div className="page-header">
          <h1 className="page-title">User Management</h1>
          <p className="page-subtitle">Add, remove, and manage access roles for all personnel.</p>
        </div>
        <div className="card">
          <div className="card-header">
            <h3>System Users</h3>
            <button className="btn-primary" onClick={() => { setShowAdd(!showAdd); setMsg(''); }}>
              {showAdd ? 'Cancel' : '+ Add User'}
            </button>
          </div>
          {showAdd && (
            <form className="add-form" onSubmit={handleAdd}>
              <input placeholder="Full Name" value={nu.name} onChange={e => setNu({...nu, name: e.target.value})} required />
              <input placeholder="Username" value={nu.username} onChange={e => setNu({...nu, username: e.target.value})} required />
              <input type="password" placeholder="Password" value={nu.password} onChange={e => setNu({...nu, password: e.target.value})} required />
              <select value={nu.role} onChange={e => setNu({...nu, role: e.target.value})}>
                <option value="researcher">Researcher</option>
                <option value="conservation_officer">Conservation Officer</option>
                <option value="forest_department">Forest Department</option>
              </select>
              <div className="full-width">
                <button type="submit" className="btn-primary">Create User</button>
                {msg && <span className="success-msg">{msg}</span>}
              </div>
            </form>
          )}
          <table className="data-table">
            <thead><tr><th>Name</th><th>Username</th><th>Role</th></tr></thead>
            <tbody>{users.map((u, i) => (
              <tr key={i}>
                <td>{u.name}</td><td><code>{u.username}</code></td>
                <td><span className={`role-badge rb-${u.role}`}>{ROLE_LABELS[u.role]}</span></td>
              </tr>
            ))}</tbody>
          </table>
        </div>
      </div>
    );

    if (activeTab === 'Dashboard') return (
      <div className="scroll-area">
        <div className="page-header">
          <h1 className="page-title">Admin Control Panel</h1>
          <p className="page-subtitle">Overview of system health, active users, and recent detections.</p>
        </div>

        <div className="stats-grid">
          <StatCard icon={<SvgUsers/>} color="blue" label="Total Users" value={users.length} trend="Active accounts" />
          <StatCard icon={<SvgCamera/>} color="green" label="Images Processed" value="42,891" trend="↑ 12% this week" trendType="pos" />
          <StatCard icon={<SvgAlert/>} color="amber" label="Species Tracked" value="1,492" trend="- Stable" />
          <StatCard icon={<SvgAlert/>} color="red" label="Poaching Alerts" value="3" trend="Requires attention" trendType="neg" />
        </div>

        <div className="two-col">
          <div className="card">
            <div className="card-header">
              <h3>System Activity</h3>
            </div>
            <p style={{color: 'var(--text-md)', fontSize: '0.95rem', lineHeight: '1.6'}}>
              The intelligence system is operating normally across all nodes. Real-time CPU computation load is at 45% and PostgreSQL dataset connections are fully stable.
              <br/><br/>
              <i>Note: Expanded system diagnostics and database analytics will go live in Milestone 2.</i>
            </p>
          </div>
          <div className="card">
            <div className="card-header"><h3>Recent Detections</h3></div>
            <DetectionList />
          </div>
        </div>
      </div>
    );

    return <GenericScreen title={activeTab} />;
  };

  return (
    <div className="app-layout">
      <TopNavbar user={user} onLogout={onLogout} />
      <div className="app-body">
        <Sidebar user={user} onLogout={onLogout} activeTab={activeTab} setActiveTab={setActiveTab} />
        <main className="main-content">
          {renderContent()}
        </main>
      </div>
    </div>
  );
}

function ResearcherDashboard({ user, onLogout }) {
  const [activeTab, setActiveTab] = useState('Dashboard');
  
  const renderContent = () => {
    if (activeTab === 'Settings') return <SettingsPage />;
    if (activeTab === 'Alerts') return <AlertsPage />;
    
    if (activeTab === 'Datasets') return (
      <div className="scroll-area">
        <div className="page-header">
          <h1 className="page-title">Dataset Management</h1>
          <p className="page-subtitle">Review, integrate, and validate wildlife data sources.</p>
        </div>
        <div className="card">
          <div className="card-header">
             <h3>Integrated Datasets</h3>
             <button className="btn-outline">Sync Remote</button>
          </div>
          <table className="data-table">
            <thead><tr><th>Dataset</th><th>Type</th><th>Records</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td>Snapshot Serengeti</td><td>Camera Trap Images</td><td>1.2M</td><td><span className="role-badge rb-researcher">Active</span></td></tr>
              <tr><td>iNaturalist Mini</td><td>Species Observations</td><td>50</td><td><span className="role-badge rb-researcher">Active</span></td></tr>
              <tr><td>GBIF Occurrences</td><td>Geo-tagged JSON</td><td>4 Species</td><td><span className="role-badge rb-researcher">Active</span></td></tr>
              <tr><td>Animal Kingdom</td><td>Video Segments</td><td>50 hrs</td><td><span className="role-badge rb-researcher">Active</span></td></tr>
              <tr><td>BirdCLEF Audio</td><td>Bioacoustic Audio</td><td>264 clips</td><td><span className="role-badge rb-forest_department">Pending</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    );

    if (activeTab === 'Dashboard') return (
      <div className="scroll-area">
        <div className="page-header">
          <h1 className="page-title">Research Workspace</h1>
          <p className="page-subtitle">Analyze species data, process images, and review audio detections.</p>
        </div>
        
        <div className="stats-grid">
          <StatCard icon={<SvgCamera/>} color="green" label="Images Analyzed" value="18,403" trend="↑ 8% this month" trendType="pos" />
          <StatCard icon={<SvgMusic/>} color="blue" label="Audio Clips" value="4,291" trend="↑ 3% this month" trendType="pos" />
          <StatCard icon={<SvgMap/>} color="amber" label="Species Identified" value="312" trend="42 new this week" trendType="pos" />
          <StatCard icon={<SvgFile/>} color="green" label="Reports Published" value="27" trend="This quarter" />
        </div>

        <div className="two-col">
          <div className="card">
            <div className="card-header"><h3>Analysis Pipeline Status</h3></div>
            <p style={{color: 'var(--text-md)', fontSize: '0.95rem', lineHeight: '1.6'}}>
              Deep learning models (YOLOv8) are loaded and active. Background bioacoustic extraction using Librosa is operating on standard priority queues.
              <br/><br/>
              <i>To view individual datasets and trigger manual retraining, navigate to the <strong>Datasets</strong> tab.</i>
            </p>
          </div>
          <div className="card">
            <div className="card-header"><h3>Recent Detections</h3></div>
            <DetectionList />
          </div>
        </div>
      </div>
    );

    return <GenericScreen title={activeTab} />;
  };

  return (
    <div className="app-layout">
      <TopNavbar user={user} onLogout={onLogout} />
      <div className="app-body">
        <Sidebar user={user} onLogout={onLogout} activeTab={activeTab} setActiveTab={setActiveTab} />
        <main className="main-content">
          {renderContent()}
        </main>
      </div>
    </div>
  );
}

function OfficerDashboard({ user, onLogout }) {
  const [activeTab, setActiveTab] = useState('Dashboard');

  const renderContent = () => {
    if (activeTab === 'Settings') return <SettingsPage />;
    if (activeTab === 'Alerts') return <AlertsPage />;

    if (activeTab === 'Dashboard') return (
      <div className="scroll-area">
        <div className="page-header">
          <h1 className="page-title">Conservation Command Center</h1>
          <p className="page-subtitle">Monitor threats, manage alerts, and coordinate field teams.</p>
        </div>
        
        <div className="stats-grid">
          <StatCard icon={<SvgAlert/>} color="red" label="Active Alerts" value="3" trend="Immediate action" trendType="neg" />
          <StatCard icon={<SvgMap/>} color="green" label="Protected Zones" value="14" trend="All secure" trendType="pos" />
          <StatCard icon={<SvgUsers/>} color="blue" label="Field Teams" value="8" trend="3 on patrol" />
          <StatCard icon={<SvgMap/>} color="amber" label="Tracked Animals" value="67" trend="With GPS collars" />
        </div>

        <div className="two-col">
          <div className="card">
            <div className="card-header"><h3>Field Overview</h3></div>
            <p style={{color: 'var(--text-md)', fontSize: '0.95rem', lineHeight: '1.6'}}>
              All remote patrol teams are transmitting stable GPS heartbeat signals. Weather conditions remain optimal for continued monitoring.
              <br/><br/>
              <i>To respond to high-priority threat vectors, navigate to the <strong>Alerts</strong> tab. Real-time team geofencing goes live next patch.</i>
            </p>
          </div>
          <div className="card">
            <div className="card-header"><h3>Recent Detections</h3></div>
            <DetectionList />
          </div>
        </div>
      </div>
    );

    return <GenericScreen title={activeTab} />;
  };

  return (
    <div className="app-layout">
      <TopNavbar user={user} onLogout={onLogout} />
      <div className="app-body">
        <Sidebar user={user} onLogout={onLogout} activeTab={activeTab} setActiveTab={setActiveTab} />
        <main className="main-content">
          {renderContent()}
        </main>
      </div>
    </div>
  );
}

function ForestDashboard({ user, onLogout }) {
  const [activeTab, setActiveTab] = useState('Dashboard');

  const renderContent = () => {
    if (activeTab === 'Settings') return <SettingsPage />;
    if (activeTab === 'Alerts' || activeTab === 'Incidents') return <AlertsPage />;
    
    if (activeTab === 'Patrol Zones') return (
      <div className="scroll-area">
        <div className="page-header">
          <h1 className="page-title">Patrol Zones</h1>
          <p className="page-subtitle">Manage assignments and review zone statuses.</p>
        </div>
        <div className="card">
          <div className="card-header">
            <h3>Patrol Zone Status</h3>
            <button className="btn-outline">Dispatch Team</button>
          </div>
          <table className="data-table">
            <thead><tr><th>Zone</th><th>Status</th><th>Last Patrol</th><th>Officer</th></tr></thead>
            <tbody>
              <tr><td>North Corridor A</td><td><span className="role-badge rb-researcher">Clear</span></td><td>Today 06:00</td><td>Team Alpha</td></tr>
              <tr><td>South Reserve B</td><td><span className="role-badge rb-researcher">Clear</span></td><td>Today 08:30</td><td>Team Bravo</td></tr>
              <tr><td>East Buffer Zone</td><td><span className="role-badge rb-admin">Alert</span></td><td>Yesterday</td><td>Unassigned</td></tr>
              <tr><td>West Corridor C</td><td><span className="role-badge rb-researcher">Clear</span></td><td>Today 07:15</td><td>Team Charlie</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    );

    if (activeTab === 'Dashboard') return (
      <div className="scroll-area">
        <div className="page-header">
          <h1 className="page-title">Forest Department Portal</h1>
          <p className="page-subtitle">Monitor forest health, patrol zones, and wildlife corridor activity.</p>
        </div>
        
        <div className="stats-grid">
          <StatCard icon={<SvgMap/>} color="green" label="Forest Zones" value="32" trend="Under surveillance" trendType="pos" />
          <StatCard icon={<SvgMap/>} color="blue" label="Patrol Routes" value="9" trend="Active today" />
          <StatCard icon={<SvgAlert/>} color="red" label="Fire Risk Zones" value="2" trend="Monitor closely" trendType="neg" />
          <StatCard icon={<SvgMap/>} color="amber" label="Wildlife Corridors" value="5" trend="All open" trendType="pos" />
        </div>

        <div className="two-col">
          <div className="card">
            <div className="card-header"><h3>Zone Overview</h3></div>
            <p style={{color: 'var(--text-md)', fontSize: '0.95rem', lineHeight: '1.6'}}>
              Overall thermal anomaly detection indicates that fire risk remains extremely low today. Wildlife corridors C and D are clear of obstruction.
              <br/><br/>
              <i>To view granular details about specific sectors and teams, navigate to the <strong>Patrol Zones</strong> tab.</i>
            </p>
          </div>
          <div className="card">
            <div className="card-header"><h3>Recent Detections</h3></div>
            <DetectionList />
          </div>
        </div>
      </div>
    );

    return <GenericScreen title={activeTab} />;
  };

  return (
    <div className="app-layout">
      <TopNavbar user={user} onLogout={onLogout} />
      <div className="app-body">
        <Sidebar user={user} onLogout={onLogout} activeTab={activeTab} setActiveTab={setActiveTab} />
        <main className="main-content">
          {renderContent()}
        </main>
      </div>
    </div>
  );
}

function LoginScreen({ users, onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const found = users.find(u => u.username === username && u.password === password);
    if (found) onLogin(found);
    else setError('Invalid username or password.');
  };

  return (
    <div className="login-page">
      <div className="login-overlay" />
      <div className="login-card">
        <div className="login-top-bar">
          <LeafIcon />
          <h1 style={{marginTop: '10px'}}>Wildlife Intelligence</h1>
          <p>Population Monitoring System</p>
        </div>
        <div className="login-body">
          <form onSubmit={handleSubmit}>
            <div className="field-group">
              <label>Username</label>
              <input type="text" value={username} onChange={e => setUsername(e.target.value)} placeholder="Enter username" required />
            </div>
            <div className="field-group">
              <label>Password</label>
              <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Enter password" required />
            </div>
            {error && <div className="err-msg">{error}</div>}
            <button type="submit" className="btn-login">Authenticate</button>
          </form>
          <div className="rbac-tag">Role-Based Access Control Enabled</div>
        </div>
      </div>
    </div>
  );
}

export default function App() {
  const [users, setUsers] = useState(initialUsers);
  const [currentUser, setCurrentUser] = useState(null);

  if (!currentUser) return <LoginScreen users={users} onLogin={setCurrentUser} />;
  
  const props = { user: currentUser, onLogout: () => setCurrentUser(null) };
  
  if (currentUser.role === 'admin') return <AdminDashboard {...props} users={users} setUsers={setUsers} />;
  if (currentUser.role === 'researcher') return <ResearcherDashboard {...props} />;
  if (currentUser.role === 'conservation_officer') return <OfficerDashboard {...props} />;
  return <ForestDashboard {...props} />;
}
