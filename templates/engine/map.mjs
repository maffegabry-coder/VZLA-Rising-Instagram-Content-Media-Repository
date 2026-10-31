import fs from 'fs'; import * as topo from 'topojson-client'; import {geoMercator, geoPath} from 'd3-geo';
const w=JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-10m.json'));
const all=topo.feature(w,w.objects.countries);
const ven=all.features.find(f=>f.id==='862');
const out={};
function make(name,W,H,feature,pts,pad=0){
  const proj=geoMercator().fitExtent([[pad,pad],[W-pad,H-pad]],feature);
  const p=geoPath(proj);
  const neighbors=all.features.filter(f=>['170','076','328','780','533','531'].includes(f.id)).map(f=>p(f)).join(' ');
  out[name]={d:p(ven),nb:neighbors,pts:Object.fromEntries(Object.entries(pts).map(([k,[lat,lon]])=>[k,proj([lon,lat]).map(v=>+v.toFixed(1))]))};
}
const P={angel:[5.9675,-62.5356],roques:[11.95,-66.67],bolivar:[8.5414,-71.0461],roraima:[5.143,-60.762],llanos:[7.06,-69.50],caracas:[10.48,-66.90],margarita:[10.99,-63.93]};
make('ven',880,700,ven,P,10);
// Margarita zoom: bbox feature
const box={type:'Feature',geometry:{type:'Polygon',coordinates:[[[-64.44,10.875],[-64.44,11.19],[-63.77,11.19],[-63.77,10.875],[-64.44,10.875]]]}};
make('marg',880,620,box,{porlamar:[10.957,-63.85],asuncion:[11.033,-63.862],pampatar:[11.0,-63.80],juangriego:[11.08,-63.965],airport:[10.912,-63.967],restinga:[10.995,-64.05],macanao:[11.06,-64.26]},40);
fs.writeFileSync('maps.json',JSON.stringify(out));
console.log(out.ven.pts, out.marg.pts, out.ven.d.length);
